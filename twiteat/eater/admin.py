from django.contrib import admin
from models import *

class CategoryAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)