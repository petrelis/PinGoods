from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

class BlogSearchView(ListView):
    model= Blog
    template_name ='home.html'
    context_object_name = 'posts'
    
  def get_queryset(self):
      query= self.request.GET.get('search')
      return Blog.objects.filter(title__icontains=query).order_by('-created_at')


def searchbar (request):
    if request.method == 'GET' :
        search = request.GET.get('search')
        post= Post.objects.all ().filter(content_contains=result)
        return render (request, 'searchbar.html, {'post': post})