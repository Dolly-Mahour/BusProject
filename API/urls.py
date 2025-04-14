from django.urls import path
from API import views
from signup_API.views import Application_Users_View,Application_Users_Details
urlpatterns = [
    # path('students/', views.StudentView),
    path('users/', Application_Users_View.as_view()),
     path('users/<pk>', Application_Users_Details.as_view()),
]