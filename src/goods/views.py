from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from mysite.settings import GOOGLE_MAPS_API_KEY
from .models import Offer, Review, Category
from datetime import datetime
from django.utils import timezone
from django.views import generic
import requests
from urllib.parse import urlencode
from geopy.distance import lonlat, distance
from main.models import Profile

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

def MainView(request):
    user = request.user
    isseller=False
    iscustomer=False
    if user!=None:    
        profile = Profile.objects.get(user_id=user)
        isseller=profile.isseller
        iscustomer=profile.iscustomer
    if request.method == 'GET' :
        search = request.GET.get('search')
        addressSearch = request.GET.get('addressSearch')

        offers_all = Offer.objects.all()
        if search:
            offer = offers_all.filter(offer_title__icontains=search)
        else: offer = offers_all.filter(offer_price = -1)
        if offer.exists():
            lat = offer.first().offer_coords_lat
            lng = offer.first().offer_coords_lng
        else:
            lat = extract_lat_lng("Vilnius")[0]
            lng = extract_lat_lng("Vilnius")[1]

        offerAndDist = []

        if addressSearch:
            user_coords_lat = extract_lat_lng(addressSearch)[0]
            user_coords_lng = extract_lat_lng(addressSearch)[1]
            user_location = (user_coords_lat, user_coords_lng)
            for off in offer:
                offer_location = (off.offer_coords_lat, off.offer_coords_lng)
                offer_distance = (distance(user_location, offer_location).km)
                offerAndDist.append({
                    'title': off.offer_title,
                    'distance': offer_distance
                })
        else:
            user_coords_lat = 0
            user_coords_lng = 0

        context = {
            'offers_all': offers_all,
            'offer': offer,
            'offerAndDist': offerAndDist,
            'Lat': lat,
            'Lng': lng,
            'user_coords_lat': user_coords_lat,
            'user_coords_lng': user_coords_lng,
            'range': range(len(offerAndDist))
        }
        if isseller==True:
            return render (request, "goods/mainseller.html", context)
        elif iscustomer==True:
            return render (request, "goods/maincustomer.html", context)
        else:
            return render (request, "goods/mainguest.html", context)

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
                offer_coords_lat = extract_lat_lng(address)[0],
                offer_coords_lng = extract_lat_lng(address)[1],
                pub_date=date,
                offer_image='default.jpg')
            offer.save()
            return redirect("/goods")
    return render(request, "goods/addoffer.html", {"offers": offers, "categories":categories})

@login_required
def AddReview(request, offer_id):
    reviews = Review.objects.all()
    offer = get_object_or_404(Offer, pk=offer_id)
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