from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,"template.html")

# def signup(request):
#     return render(request,"signup_form.html")
