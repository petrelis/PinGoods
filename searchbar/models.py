class Blog(models.Model):
    title = models.CharField(max_length=1000)
    posts = models.TextField() 
    slug = models.SlugField(max_length=1000) 
    