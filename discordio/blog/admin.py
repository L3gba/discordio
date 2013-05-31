from django.contrib import admin
from models import *

class AuthorAdmin(admin.ModelAdmin):
    pass


class ArticleAdmin(admin.ModelAdmin):
    pass


class ImagesAdmin(admin.ModelAdmin):
    pass


class CategoriesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Categories, CategoriesAdmin)