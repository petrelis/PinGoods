from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from mysite.settings import GOOGLE_MAPS_API_KEY
from .models import Offer, Review, Category
from datetime import datetime
from django.utils import timezone
from django.views import generic
import requests
from urllib.parse import urlencode

class Index(generic.ListView):
    template_name = 'goods/index.html'
    context_object_name = 'latest_offer_list'

    def get_queryset(self):
        """
        Return the last five published offers (not including those set to be
                                                  published in the future).
        """
        return Offer.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
   model = Offer
   template_name = 'goods/detail.html'
   def get_queryset(self):
       """
       Excludes any questions that aren't published yet.
       """
       return Offer.objects.filter(pub_date__lte=timezone.now())

def MainView(request):
    if request.method == 'GET' :
        search = request.GET.get('search')
        offer = Offer.objects.all().filter(offer_title=search)
        if offer.exists():
            address = offer.values('offer_address')
        else:
            address = "Vilnius"
        lat = extract_lat_lng(address)[0]
        lng = extract_lat_lng(address)[1]
        context = {
            'offer': offer,
            'Lat': lat,
            'Lng': lng
        }
        return render (request, "goods/main.html", context)

def extract_lat_lng(address_or_postalcode, data_type = 'json'):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address": address_or_postalcode, "key": GOOGLE_MAPS_API_KEY}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200, 299): 
        return {}
    latlng = {}
    try:
        latlng = r.json()['results'][0]['geometry']['location']
    except:
        pass
    return latlng.get("lat"), latlng.get("lng")



@login_required
def AddOffer(request):
    offers = Offer.objects.all()
    categories = Category.objects.all()
    if request.method == "POST": 
        if "offerAdd" in request.POST: 
            current_user = request.user
            chosen_category = request.POST["category_select"]
            title = request.POST["title"]
            text = request.POST["text"]
            price = request.POST["price"]
            phonenumber = request.POST["phonenumber"]
            address = request.POST["address"]
            date = datetime.now()
            offer = Offer(
                user=current_user,
                category=Category.objects.get(category_name=chosen_category),
                offer_title=title, 
                offer_text=text, 
                offer_price=price,
                offer_phonenumber=phonenumber,
                offer_address=address,
                pub_date=date)
            offer.save()
            return redirect("/goods")
    return render(request, "goods/addoffer.html", {"offers": offers, "categories":categories})

@login_required
def AddReview(request, offer_id):
    reviews = Review.objects.all()
    offer = get_object_or_404(Offer, pk=offer_id)
    print(offer)
    print("Hello")
    if request.method == "POST": 
        if "reviewAdd" in request.POST: 
            current_user = request.user
            text = request.POST["text"]
            rating = request.POST["rating"]
            date = datetime.now()
            review = Review(
                offer=offer,
                author=current_user,
                review_text=text, 
                rating=rating, 
                pub_date=date)
            review.save()
            return redirect("/goods/" + str(offer_id))
    return render(request, "goods/addreview.html", {"reviews": reviews})