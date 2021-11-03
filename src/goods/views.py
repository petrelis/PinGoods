from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Offer
from datetime import datetime
from django.utils import timezone
from django.views import generic

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

@login_required
def AddOffer(request):
    offers = Offer.objects.all()
    if request.method == "POST": 
        if "offerAdd" in request.POST: 
            current_user = request.user
            title = request.POST["title"]
            text = request.POST["text"]
            category = request.POST["category"]
            price = request.POST["price"]
            date = datetime.now()
            offer = Offer(
                user=current_user,
                offer_title=title, 
                offer_text=text, 
                offer_category=category, 
                offer_price=price,
                pub_date=date)
            offer.save()
            return redirect("/")
    return render(request, "goods/addoffer.html", {"offers": offers})