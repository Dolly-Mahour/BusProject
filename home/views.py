from django.shortcuts import render,redirect
from .api_consumer import post_to_signup_api,post_login_data,get_from_place_api,post_to_search_api
from django.http import JsonResponse    
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages

import winrt.windows.devices.geolocation as wdg
import asyncio

# from django.http import HttpResponse
# from datetime import  date, datetime, time , timedelta
# import requests

token_exist = False 
jwt_token = None


def to_check_jwt():
    if jwt_token is not None :
        token_exist = True
    else :
        token_exist = False
    
    return token_exist



# --------------------LOCATION---------------------------------------------------------

async def get_coords():
        locator = wdg.Geolocator()
        pos = await locator.get_geoposition_async()
        return [pos.coordinate.latitude, pos.coordinate.longitude]

def get_location():
        return asyncio.run(get_coords())


#---------------------------------------------------------------------------------------



# MAIN HOME PAGE FUNTION CALLING AT THE START OF THE SITE
def homepage(request):
    context = get_cities(request)
    global token_exist
    global jwt_token


    latitude, longitude = get_location()
    print(f"here is the -----------Latitude: {latitude}, Longitude: {longitude}")
    
    # jwt_token = None
    token_exists_or_not = to_check_jwt()
    
    print("this is the token boolean",token_exists_or_not)
    data = {
        'cities' : context["cities"],
        'states': context["states"],
        'token': token_exists_or_not,
    }
    return render(request,"busify.html",data)


# user signup function calling the api for signup
@csrf_exempt
def signup_api_view(request):
    #if the method is post 
    if request.method == 'POST':
        try:
            #converting the data into the json to sent it to api 
            data ={
                "Username": request.POST.get('username'),
                "User_or_Agent": True,
                "Email": request.POST.get('email'),
                "Phone_number": request.POST.get('number'),
                "Password": request.POST.get('password'),
                "Referral_code": request.POST.get('ref-code')
            }
            # SIGNUP API RESPONSE and calling the api for the user signup
            result = post_to_signup_api(data)
            return JsonResponse(result or {"error": "Invalid JSON"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Only POST allowed"}, status=405)


#LOGIN Api calling and storing the jwt token into the session
@csrf_exempt
def login_api_view(request):
    #if the method is post 
    if request.method == 'POST':
        try:
            #converting the data into the json to sent it to api 
            data ={
                "Phone_number": request.POST.get('number'),
                "Password": request.POST.get('password'),
            }
            #calling the api consuming fuction for user login
            result = post_login_data(data)
            print(result)
            if result["status"] == 200 :
                if result["token"] is not None:
                    global jwt_token
                    jwt_token = result["token"]
                else :
                    
                    jwt_token = None
                #jwt token to session
                request.session["jwt_token"] = jwt_token
                #redirecting tp the homepage
                return redirect('/')
            
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    

    return JsonResponse({"error": "Only POST allowed"}, status=405)



#Funtion calling the cities api and getting the data from the api also converting it to the lists
@csrf_exempt
def get_cities(request):
    data = get_from_place_api(request)
    cities =[]#list of cities 
    states =[]#list of states
    
    #loop for entering the cities and states to the list 
    for i in data:
        cities.append(i["cities"])
        # print(cities)
        states.append(i["states"])
    
    #data context dictoinary 
    context = {
        'cities' : cities,
        'states' : states,
    }
    return context

@csrf_exempt
def search_api_view(request):
    #if the method is post 
    # print(request)
    if request.method == 'POST':
        print(request)
        try:
            #converting the data into the json to sent it to api 
            data ={
                "from_place_id": request.POST.get('from_place'),
                "to_place_id": request.POST.get('to_place'),
                "date": request.POST.get('date'),
            }
            # SIGNUP API RESPONSE and calling the api for the user signup
            result = post_to_search_api(data)
            return JsonResponse(result or {"error": "Invalid JSON"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Only POST allowed"}, status=405)