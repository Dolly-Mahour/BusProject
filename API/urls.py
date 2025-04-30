from django.urls import path
from signup_API.views import Application_Users_View
from login_API.views import Login_User_Views
from cities_API.views import places_View
from Search_Places_API.views import Search_Places_view


urlpatterns = [
    path('places/', places_View.as_view()),
    path('users/', Application_Users_View.as_view()),
    path('login/', Login_User_Views.as_view()),
    path('search_trip/',Search_Places_view.as_view()),
    # primary key based functions urls
    #  path('users/<pk>', Application_Users_Details.as_view()),
]