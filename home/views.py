from django.shortcuts import render,redirect
from datetime import  date, datetime, time , timedelta
from calendar import HTMLCalendar,mdays


def homepage(request):
    theme_ = "Light"
    theme = "off"
    if request.method == "POST":
         theme = request.POST.get('theme_change')
         if theme == "on" :
             theme_ = "Dark"
         else :
             theme_ = "Light"
                   
    context = {
        'theme_' :theme_,
        'theme' : theme
    }
    return render(request,"busify.html",context)

def set_session(request):
    # current_language = request.POST
    request.session['language_to_set'] = 'hindi'
    return render(request,"working.html",)