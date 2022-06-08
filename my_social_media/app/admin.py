from django.contrib import admin
from .models import Tweet, Followers

# Register your models here.

admin.site.register(Tweet)
admin.site.register(Followers)