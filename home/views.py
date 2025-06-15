from django.shortcuts import render,redirect
from django.template.response import TemplateResponse
from .api_consumer import post_to_signup_api,post_login_data,get_from_place_api,post_to_search_api
from django.http import JsonResponse    
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages



# token is not exist when user is not logged in 
token_exist = False 
# we do not have jwt token 
jwt_token = None
# the default code response of signup api 
http_code_of_singup_api = 401
# the default code response of login api 
http_code_of_login_api = 400
# the default message response of login api 
login_response_message = None
# the default message response of login api 
signup_response_message = None
# user profile first letter of name is empty 
profile = ""
# the user object that contain the information of the logged in user
User ={}
# list of the flags and with the image sources 
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


# method that checks that jwt token exists or not
def to_check_jwt():
    if jwt_token is not None :
        token_exist = True
    else :
        token_exist = False
    
    return token_exist


def getdata():
    global token_exist
    global jwt_token
    global http_code_of_singup_api
    global profile
    global flag_and_language
    token_exists_or_not = to_check_jwt()
    http_code_of_singup_api= 401
    data = {
        'token': token_exists_or_not,
        'http_code_of_singup_api' : http_code_of_singup_api,
        'profile' : profile,
        'User':User,
        'flag_and_language':flag_and_language,
        'http_code_of_singup_api':http_code_of_singup_api,
    }
    return data

# MAIN HOME PAGE FUNTION CALLING AT THE START OF THE SITE
def homepage(request):
    # all the global variables we are using in the home page 
    global token_exist
    global jwt_token
    global http_code_of_singup_api
    global profile
    global http_code_of_login_api 
    global login_response_message
    global User         
    global flag_and_language
    global signup_response_message
    # get api of the cities 
    CitiesList = get_cities(request)
    # to check token
    token_exists_or_not = to_check_jwt()
    
    print("IS TOKEN EXIST-->",token_exists_or_not)
    print("IS USER SIGNED UP-->",http_code_of_singup_api)
    print("IS USER LOGGED IN -->",User)
    
    data = {
        'cities' : CitiesList["cities"],
        'states': CitiesList["states"],
        'token': token_exists_or_not,
        'http_code_of_singup_api' : http_code_of_singup_api,
        'profile' : profile,
        'flag_and_language':flag_and_language,
        'User':User,
        'http_code_of_login_api':http_code_of_login_api,
        'login_response_message':login_response_message,
        'signup_response_message':signup_response_message,
    }

    # set the code value again to default 
    http_code_of_login_api = 400
    http_code_of_singup_api= 401 
    # render to the home page  
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
            global signup_response_message
            http_code_of_singup_api = result['status']
            signup_response_message= result['message']
            print("SIGNUP API RESPONSE-->",http_code_of_singup_api)
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
            global profile
            print("RETURNING RESULT OF LOGIN API -->",result)
            # if status code is 200 ok
            if result["status"] == 200 : 
                # and token is generated through api
                if result["token"] is not None:
                    # get the jwt token 
                    jwt_token = result["token"]
                    # get the status code 
                    http_code_of_login_api = result['status']
                    # get the response message
                    login_response_message = result['message']
                    # find the first letter of the username 
                    User = result["User"] 
                    User = User[0]
                    Username = User["Username"]
                    profile = Username[0]
                    print("IS JWT EXIST-->",jwt_token)
                # if success code is 401 or invalid information
                else :
                    print("NO JWT TOKEN FOUND--!")
                # storing the token in the session 
                request.session["jwt_token"] = jwt_token
                print("USERNAME FIRST LETTER -->",profile)
                # redirecting to the homepage
                return redirect('/')
            else:
                print("GETTING THE INVALID CREDENTIALS --!")
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
    cities =[]  #list of cities 
    states =[]  #list of states
    
    #loop for entering the cities and states to the list 
    for i in data:
        cities.append(i["cities"])
        # print(cities)
        states.append(i["states"])
    
    #data CitiesList dictoinary 
    CitiesList = {
        'cities' : cities,
        'states' : states,
    }
    return CitiesList

@csrf_exempt
def search_api_view(request):
    #if the method is post 
    if request.method == 'POST':
        # id and date entered by user 
        from_place = request.POST.get('from_place')
        to_place = request.POST.get('to_place')
        on_date = request.POST.get('date')
        # check if they are not selected
        if(from_place == 'place' or to_place == 'place' or on_date == None):
            return redirect('/')
        try:
            data ={
                "from_place_id": request.POST.get('from_place'),
                "to_place_id": request.POST.get('to_place'),
                "date": request.POST.get('date'),
            }
            global token_exist
            global jwt_token
            global http_code_of_singup_api
            global profile
            global flag_and_language
            http_code_of_singup_api= 401
            # calling the searching bus api
            result = post_to_search_api(data)
            # get list of citites
            CitiesList = get_cities(request)
            city_obj = None
            state_obj = None
            token_exists_or_not = to_check_jwt()
           
            if "data" not in result :
                result["data"] = None 
            else:
                # search_result_objects = result["data"]
                from_id = request.POST.get('from_place')
                from_id = int(from_id)
                to_id = request.POST.get('to_place')
                to_id = int(to_id)
                cities = CitiesList["cities"]
                states = CitiesList["states"]
                city_obj = {
                    "from":cities[from_id],
                    "to":cities[to_id],
                }
                state_obj = {
                    "from":states[from_id],
                    "to":states[to_id],
                }
                token_exists_or_not = to_check_jwt()
            
            data = {
                    'cities' : CitiesList["cities"],
                    'states': CitiesList["states"],
                    'token': token_exists_or_not,
                    'http_code_of_singup_api' : http_code_of_singup_api,
                    'profile' : profile,
                    'search_results':result["data"],
                    'city_obj':city_obj,
                    'state_obj':state_obj,
                    'flag_and_language':flag_and_language,

            }
            return render(request,"search_bus_page.html",data)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Only POST allowed"}, status=405)




def myprofile(request):
    # calling the method of geting the global data used on the ui 
    data = getdata()
    # rendering to myprofie page
    return render(request,"myprofile.html",data)


def PrivacyAndPolicy(request):
    # calling the method of geting the global data used on the ui 
    data = getdata()
    print("DATA IN PRIVACY POLICY FUNCTION-->",data)
    # rendering to myprofie page
    return render(request,"PrivacyAndPolicy.html",data)
    
def TermAndConditions(request):
    # calling the method of geting the global data used on the ui 
    data = getdata()
    # rendering to myprofie page
    return render(request,"TermAndConditions.html",data)
    
def ContactUs(request):
    # calling the method of geting the global data used on the ui 
    data = getdata()
    # rendering to myprofie page
    return render(request,"ContactUs.html",data)
    
def CancellationPolicy(request):
    # calling the method of geting the global data used on the ui 
    data = getdata()
    # rendering to myprofie page
    return render(request,"CancellationPolicy.html",data)
    
def MyTickets(request):
    # calling the method of geting the global data used on the ui 
    data = getdata()
    # rendering to myprofie page
    return render(request,"MyTickets.html",data)
    
def MyWallet(request):
    # calling the method of geting the global data used on the ui 
    data = getdata()
    # rendering to myprofie page
    return render(request,"MyWallet.html",data)

def RefferAndEarn(request):
    # calling the method of geting the global data used on the ui 
    data = getdata()
    # rendering to myprofie page
    return render(request,"RefferAndEarn.html",data)

# function for loggin out account all the global variables et to null and to the default value and whole data is refreshed
def Account_Logout(request):
    global token_exist
    global jwt_token
    global http_code_of_singup_api
    global profile
    global http_code_of_login_api 
    global login_response_message
    global User         
    global flag_and_language
    global signup_response_message

    token_exist = False 
    jwt_token = None
    http_code_of_singup_api = 401
    http_code_of_login_api = 400
    login_response_message = None
    signup_response_message = None
    profile = ""
    User ={}
    return redirect("/")





# --------------------LOCATION---------------------------------------------------------

# async def get_coords():
#         locator = wdg.Geolocator()
#         pos = await locator.get_geoposition_async()
#         return [pos.coordinate.latitude, pos.coordinate.longitude]

# def get_location():
#         return asyncio.run(get_coords())


#---------------------------------------------------------------------------------------

