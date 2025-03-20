from django.contrib import admin
from .models import post
from parler.admin import TranslatableAdmin 
# Register your models here.
admin.site.register(post, TranslatableAdmin)
