from django.db import models

class Categories(models.Model):
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
    
    
class Images(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    
    def __unicode__(self):
        return self.title
    
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    categories = models.ManyToManyField(Categories)
    images = models.ManyToManyField(Images)
    
    def __unicode__(self):
        return self.title