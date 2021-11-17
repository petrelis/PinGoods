def searchbar (request):
    if request.method == 'GET' :
        search = request.GET.get('search')
        post= Post.objects.all ().filter(content_contains=result)
        return render (request, 'searchbar.html, {'post': post})