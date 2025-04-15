from django.urls import path
from API import views
from signup_API.views import Application_Users_View
from login_API.views import Login_User_Views
urlpatterns = [
    # path('students/', views.StudentView),
    path('users/', Application_Users_View.as_view()),
    path('login/', Login_User_Views.as_view()),
    #  path('users/<pk>', Application_Users_Details.as_view()),
]