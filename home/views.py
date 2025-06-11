from django.shortcuts import render,redirect
from django.template.response import TemplateResponse
from .api_consumer import post_to_signup_api,post_login_data,get_from_place_api,post_to_search_api
from django.http import JsonResponse    
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages

# import winrt.windows.devices.geolocation as wdg    #this is for geolocation and for the current location  
# import asyncio

# from django.http import HttpResponse
# from datetime import  date, datetime, time , timedelta
# import requests

token_exist = False 
jwt_token = None
http_code_of_singup_api = 400
http_code_of_login_api = 400
login_response_message = None
profile = ""
User ={}
flag_and_language=[

        {'name':"Hindi",
         'src':"flag.png"},
         {'name':"English",
         'src':"united-kingdom.png"},
         {'name':"Japnese",
         'src':"japan.png"},
         {'name':"French",
         'src':"france.png"},
         {'name':"Spanish",
         'src':"spain.png"},
    ]

def to_check_jwt():
    if jwt_token is not None :
        token_exist = True
    else :
        token_exist = False
    
    return token_exist




# MAIN HOME PAGE FUNTION CALLING AT THE START OF THE SITE
def homepage(request):
    context = get_cities(request)
    global token_exist
    global jwt_token
    global http_code_of_singup_api
    global profile
    global http_code_of_login_api 
    global login_response_message
    

    # latitude, longitude = get_location()
    # print(f"here is the -----------Latitude: {latitude}, Longitude: {longitude}")
    
    # jwt_token = None
    token_exists_or_not = to_check_jwt()
    
    print("this is the token boolean",token_exists_or_not)
    print("------------success code ----------------------------------",http_code_of_singup_api)
    global User         
    global flag_and_language
    print("THIS IS THE GLOBAL USER",User)
    data = {
        'cities' : context["cities"],
        'states': context["states"],
        'token': token_exists_or_not,
        'http_code_of_singup_api' : http_code_of_singup_api,
        'profile' : profile,
        'flag_and_language':flag_and_language,
        'User':User,
        'http_code_of_login_api':http_code_of_login_api,
        'login_response_message':login_response_message,
    }
    http_code_of_login_api = 400
    http_code_of_singup_api= 400
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
            global http_code_of_singup_api
            http_code_of_singup_api = result['status']
            print("after the signup this is the success code",http_code_of_singup_api)
            return redirect('/')
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
            global login_response_message
            global jwt_token
            global http_code_of_login_api
            global login_response_message
            global User
            print("the result we are getting from the login api--------",result)
            
            if result["status"] == 200 : 
                if result["token"] is not None:
                    
                    jwt_token = result["token"]
                    http_code_of_login_api = result['status']
                    login_response_message = result['message']

                    User = result["User"] 
                    User = User[0]
                    Username = User["Username"]
                    global profile
                    profile = Username[0]
                    print("This is the jwt tokn after the login that is changing to the globar variable",jwt_token)
                    to_check_jwt()
                
                else :
                    print("token is none-------------")
                    jwt_token = None
                #jwt token to session
                request.session["jwt_token"] = jwt_token
                #redirecting to the homepage
                print("This is the getting the object",profile)
                
                return redirect('/')
            else:
                print("getting into the bad credentials ------------------")
                http_code_of_login_api = result['status']
                login_response_message = result['message']
                return redirect('/')


        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    

    return JsonResponse({"error": "Only POST-- allowed"}, status=405)



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
            result = post_to_search_api(data)

            # print("Result gettting from searching buses----------------",result)

            context = get_cities(request)
            global token_exist
            global jwt_token
            global http_code_of_singup_api
            global profile

            # print(context["cities"])

            city_obj = None
            state_obj = None
            token_exists_or_not = to_check_jwt()
           
            if "data" not in result :
                result["data"] = None 
            else:
                search_result_objects = result["data"]

                from_id = request.POST.get('from_place')
                from_id = int(from_id)
                to_id = request.POST.get('to_place')
                to_id = int(to_id)

                cities = context["cities"]
                states = context["states"]
            
                city_obj = {
                    "from":cities[from_id],
                    "to":cities[to_id],
                }
                state_obj = {
                    "from":states[from_id],
                    "to":states[to_id],
                }
                token_exists_or_not = to_check_jwt()
            global flag_and_language



            data = {
                    'cities' : context["cities"],
                    'states': context["states"],
                    'token': token_exists_or_not,
                    'http_code_of_singup_api' : http_code_of_singup_api,
                    'profile' : profile,
                    'search_results':result["data"],
                    'city_obj':city_obj,
                    'state_obj':state_obj,
                    'flag_and_language':flag_and_language,

            }
            http_code_of_singup_api = 400
            # return JsonResponse(result or {"error": "Invalid JSON"}, status=400)
            return render(request,"search_bus_page.html",data)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Only POST allowed"}, status=405)




def myprofile(request):
    # context = get_cities(request)
    global token_exist
    global jwt_token
    global http_code_of_singup_api
    global profile
    global flag_and_language
    token_exists_or_not = to_check_jwt()
    
    # print("this is the token boolean",token_exists_or_not)
    # print("------------success code ----------------------------------",http_code_of_singup_api)

    data = {
        # 'cities' : context["cities"],
        # 'states': context["states"],
        'token': token_exists_or_not,
        'http_code_of_singup_api' : http_code_of_singup_api,
        'profile' : profile,
        'User':User,
        'flag_and_language':flag_and_language,
    }
    http_code_of_singup_api = 400

    return render(request,"myprofile.html",data)









# --------------------LOCATION---------------------------------------------------------

# async def get_coords():
#         locator = wdg.Geolocator()
#         pos = await locator.get_geoposition_async()
#         return [pos.coordinate.latitude, pos.coordinate.longitude]

# def get_location():
#         return asyncio.run(get_coords())


#---------------------------------------------------------------------------------------

