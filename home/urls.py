from django.urls import path 
from .import views

urlpatterns = [

    path('',views.homepage,name='home'),
    
    # path('i18n/setlang/', set_language, name='set_language'),
]