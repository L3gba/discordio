from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name

class User(models.Model):
    short_name = models.CharField(max_length=20)
    categories = models.ManyToManyField(Category)
    
    def __unicode__(self):
        return self.short_name
    