from django.contrib import admin
from .models import MenuEntry, MenuCategory, Review

# Register your models here.
admin.site.register(MenuEntry)
admin.site.register(MenuCategory)
admin.site.register(Review)
