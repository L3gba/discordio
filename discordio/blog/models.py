from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name
    
    
class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    avatar = models.URLField()
    
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
    
    
class Image(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    
    def __unicode__(self):
        return self.title
    
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    categories = models.ManyToManyField(Category)
    images = models.ManyToManyField(Image)
    date_published = models.DateTimeField(auto_now_add=True)
    is_hot = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.title