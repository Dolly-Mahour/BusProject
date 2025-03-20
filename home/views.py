from django.shortcuts import render
from .models import post

# Create your views here.

def homepage(request):
    peoples = post.objects.all()
    
    return render(request,"busify.html", context={'peoples': peoples})

