from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import OfferEditForm
from .models import Offer, Review, Category
from datetime import datetime
from django.utils import timezone
from django.views import generic
from django.contrib import messages

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
        offer = Offer.objects.all ().filter(offer_title=search)
        return render (request, "goods/main.html", {"offer": offer})

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
                pub_date=date,
                offer_image='default.jpg')
            offer.save()
            return redirect("/goods")
    return render(request, "goods/addoffer.html", {"offers": offers, "categories":categories})

@login_required
def EditOffer(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)
    categories = Category.objects.all()
    if request.method == 'POST':
        offeredit_form = OfferEditForm(request.POST, instance=request.user)

        if offeredit_form.is_valid():
            current_user = request.user
            offer.refresh_from_db()
            Offer.objects.filter(pk=offer_id).update(offer_text = offeredit_form.cleaned_data.get('description'))
            Offer.objects.filter(pk=offer_id).update(category = offeredit_form.cleaner_data.get('gustas'))
            Offer.objects.filter(pk=offer_id).update(offer_phonenumber = offeredit_form.cleaned_data.get('phone_number'))
            Offer.objects.filter(pk=offer_id).update(offer_address = offeredit_form.cleaned_data.get('address'))
            Offer.objects.filter(pk=offer_id).update(offer_price = offeredit_form.cleaned_data.get('price'))
            #print(offer.Offer.address)
            offeredit_form.save()
            messages.success(request, 'Your offer is updated successfully')
            return redirect("/goods/" + str(offer_id))
    else:
        offeredit_form = OfferEditForm(instance=request.user)
    return render(request, "goods/offeredit.html", {"offer": offer, "categories":categories})

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