from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Offer
from datetime import datetime

@login_required
def index(request):
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
    return render(request, "goods/index.html", {"offers": offers})