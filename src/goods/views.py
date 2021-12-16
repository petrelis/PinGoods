from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from mysite.settings import GOOGLE_MAPS_API_KEY
from .models import Offer, Review, Category, Order, Favourite
from datetime import datetime
from django.utils import timezone
from django.views import generic
import requests
from urllib.parse import urlencode
from geopy.distance import lonlat, distance
from main.models import Profile
from paypal.standard.forms import PayPalPaymentsForm
from .forms import OfferEditForm
import difflib

class Index(generic.ListView):
    template_name = 'goods/index.html'
    context_object_name = 'latest_offer_list'

    def get_queryset(self):
        """
        Return the last five published offers (not including those set to be
                                                  published in the future).
        """
        return Offer.objects.filter(
            active=True,
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
    if user.id != None: 
        profile = Profile.objects.get(user_id=user)
        isseller=profile.isseller
        iscustomer=profile.iscustomer
    if request.method == 'GET' :
        search = request.GET.get('search')
        addressSearch = request.GET.get('addressSearch')

        offers_all = Offer.objects.filter(active=True)
    
        if search:
            offer_score={}
            offers=Offer.objects.filter(active=True).values_list('offer_title', flat=True)
            
            for i in offers:
                offer_score[i]=difflib.SequenceMatcher(None, search.lower(), i.lower()).ratio()
            
            results = sorted(offer_score, key=offer_score.get, reverse=True)[:2] 
            offer = offers_all.filter(offer_title__in=results)
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
                offer_distance = format((distance(user_location, offer_location).km),'.2f')
                offerAndDist.append({
                    'id':off.id,
                    'user_coords_lat': user_coords_lat,
                    'user_coords_lng': user_coords_lng,
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
    user = request.user
    profile = Profile.objects.get(user_id=user)
    if profile.isseller != True:
        return redirect("/goods/main")
    else:
        offers = Offer.objects.all()
        categories = Category.objects.all()
        if request.method == "POST": 
            if "offerAdd" in request.POST: 
                current_user = request.user
                title = request.POST["title"]
                chosen_category = request.POST["category_select"]
                quantity = request.POST["quantity"]
                price = request.POST["price"]
                address = request.POST["address"]
                paypal = request.POST["paypal"]
                phonenumber = request.POST["phonenumber"]
                text = request.POST["text"]  
                if request.method == 'POST' and 'imageinput' in request.FILES:
                    doc = request.FILES #returns a dict-like object
                    doc_name = doc['imageinput']
                else:
                    doc_name="default.jpg"
                date = datetime.now()
                offer = Offer(
                    user=current_user,
                    category=Category.objects.get(category_name=chosen_category),
                    offer_title=title, 
                    offer_text=text, 
                    offer_quantity=quantity,
                    offer_price=price,
                    offer_phonenumber=phonenumber,
                    offer_address=address,
                    offer_paypal=paypal,
                    offer_coords_lat = extract_lat_lng(address)[0],
                    offer_coords_lng = extract_lat_lng(address)[1],
                    offer_image=doc_name,
                    pub_date=date)
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
            return redirect("/goods/main")
    return render(request, "goods/addreview.html", {"reviews": reviews})

class OfferList(generic.ListView):
    template_name = 'goods/offerlist.html'
    context_object_name = 'offers'

    def get_queryset(self):
        return Offer.objects.filter(
            pub_date__lte=timezone.now(),
            active=True,
            ).order_by('-pub_date')
    
@login_required
def EditOffer(request, offer_id):
    user = request.user
    offer = get_object_or_404(Offer, pk=offer_id)
    if user==offer.user:
        categories = Category.objects.all()
        if request.method == 'POST':
            offeredit_form = OfferEditForm(request.POST, request.FILES, instance=request.user)
            if offeredit_form.is_valid():
                current_user = request.user
                offer.refresh_from_db()
                Offer.objects.filter(pk=offer_id).update(offer_title = offeredit_form.cleaned_data.get('title'))
                Offer.objects.filter(pk=offer_id).update(offer_quantity = offeredit_form.cleaned_data.get('quantity'))
                Offer.objects.filter(pk=offer_id).update(offer_phonenumber = offeredit_form.cleaned_data.get('phone_number'))
                Offer.objects.filter(pk=offer_id).update(offer_address = offeredit_form.cleaned_data.get('address'))
                Offer.objects.filter(pk=offer_id).update(offer_paypal = offeredit_form.cleaned_data.get('paypal'))
                Offer.objects.filter(pk=offer_id).update(offer_price = offeredit_form.cleaned_data.get('price'))
                Offer.objects.filter(pk=offer_id).update(offer_text = offeredit_form.cleaned_data.get('text'))
                offer.offer_coords_lat = extract_lat_lng(offeredit_form.cleaned_data.get('address'))[0]
                offer.offer_coords_lng = extract_lat_lng(offeredit_form.cleaned_data.get('address'))[1]
                offeredit_form.save()
                if request.method == 'POST' and 'image' in request.FILES:
                    doc = request.FILES #returns a dict-like object
                    doc_name = doc['image']
                else:
                    doc_name=offer.offer_image
                    offer.offer_image = doc_name
                    offer.save()
                    messages.success(request, 'Your offer is updated successfully')
                    return redirect("/goods/" + str(offer_id))
        else:
            offeredit_form = OfferEditForm(instance=request.user)
    else:
        return redirect("/goods/main")
    return render(request, "goods/offeredit.html", {"offer": offer, "categories":categories})
    
def checkout(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)
    if request.method == 'POST':
        date = datetime.now()
        o = Order(
            name = request.user,
            offer = get_object_or_404(Offer, pk=offer_id),
            email = "None",
            address = "None",
            date = date,
            paid = False,
        )
        o.save()

        request.session['order_id'] = o.id

        #messages.add_message(request, messages.INFO, 'Order Placed!')
        return redirect('/goods/' + str(offer_id) + '/process_payment')


    else:
        return render(request, 'goods/checkout.html', {"offer": offer})

def process_payment(request, offer_id):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    offer = get_object_or_404(Offer, pk=offer_id)
    host = request.get_host()

    paypal_dict = {
        'business': offer.offer_paypal,
        'amount': '%.2f' % order.total_cost(),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(0) + str(offer_id) + str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('pay:payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('pay:payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'goods/process_payment.html', {'order': order, 'form': form})

@csrf_exempt
def payment_done(request):
    return render(request, 'goods/payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'goods/payment_cancelled.html')

def FavouriteAdd(request, offer_id):
    favourites = Favourite.objects.all()
    current_user = request.user
    current_offer = get_object_or_404(Offer, pk=offer_id)
    
    if not Favourite.objects.filter(user=current_user, offer=current_offer).exists():
        favourite=Favourite(
            offer = current_offer,
            user = current_user,
            )
        favourite.save()
    else:
        Favourite.objects.filter(user=current_user, offer=current_offer).delete()
        
    return redirect('goods:main')

class FavouriteList(generic.ListView):
    template_name = 'goods/favouritelist.html'
    context_object_name = 'favourites'

    def get_queryset(self):
        return Favourite.objects.filter().order_by('offer')
    
def DeactivateOffer(request, offer_id):
    favourites = Favourite.objects.all()
    current_user = request.user
    current_offer = get_object_or_404(Offer, pk=offer_id)
    if current_user==current_offer.user:
        current_offer.active=False
        current_offer.save()
    else:
        redirect("/goods/main")
        
    return redirect('goods:offerlist')