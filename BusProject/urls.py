"""
URL configuration for BusProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path,include
from home.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView ,TokenVerifyView


urlpatterns = [
    
    
]
urlpatterns += i18n_patterns(
    # url for languages and the internationalisation 
    path('i18n/', include('django.conf.urls.i18n')),

    # url for the rosetta framework or for the languages additions 
    path('rosetta/', include('rosetta.urls')),

    # including url of the main function view of the site
    path('', include('home.urls')),

    # url of the admin pannel 
    path('admin/', admin.site.urls),

    # url of the signup form with api 
    path('signup/',signup_api_view,name='signup_api_view'),

    # url of the login form 
    path('login/',login_api_view,name='login_api_view'),

    #searching trips views
    path ('search_trips/',search_api_view,name='searching_trips'),

    # including the api urls 
    path('api/v1/', include('API.urls')),
    

    # JWT token urls for the restframework-jwt  for  get, refresh and verifying the token
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),   
    path('verifytoken/', TokenVerifyView.as_view(),name='veify_token'), 

    prefix_default_language=False
)

# static debugging 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
