from django.shortcuts import render, redirect
from django.http import JsonResponse    
from django.views.decorators.csrf import csrf_exempt
import json

from cities_API.models import place
from Search_Places_API.models import search_bus_trips
from signup_API.models import Application_Users   # अगर model का नाम अलग है तो change करो

# ---------------- GLOBALS ---------------- #

token_exist = False 
jwt_token = None
http_code_of_singup_api = 401
http_code_of_login_api = 400
login_response_message = None
signup_response_message = None
profile = ""
User = {}

flag_and_language = [
    {'name': "Hindi", 'src': "flag.png"},
    {'name': "English", 'src': "united-kingdom.png"},
    {'name': "Japnese", 'src': "japan.png"},
    {'name': "French", 'src': "france.png"},
    {'name': "Spanish", 'src': "spain.png"},
]

# ---------------- COMMON ---------------- #

def to_check_jwt():
    return jwt_token is not None


def getdata():
    return {
        'token': to_check_jwt(),
        'http_code_of_singup_api': http_code_of_singup_api,
        'profile': profile,
        'User': User,
        'flag_and_language': flag_and_language,
    }

# ---------------- HOME ---------------- #

def homepage(request):
    CitiesList = get_cities(request)

    data = {
        'cities': CitiesList["cities"],
        'states': CitiesList["states"],
        'token': to_check_jwt(),
        'http_code_of_singup_api': http_code_of_singup_api,
        'profile': profile,
        'flag_and_language': flag_and_language,
        'User': User,
        'http_code_of_login_api': http_code_of_login_api,
        'login_response_message': login_response_message,
        'signup_response_message': signup_response_message,
    }

    return render(request, "busify.html", data)

# ---------------- SIGNUP ---------------- #

@csrf_exempt
def signup_api_view(request):
    global http_code_of_singup_api, signup_response_message

    if request.method == 'POST':
        try:
            user = Application_Users.objects.create(
                Username=request.POST.get('username'),
                Email=request.POST.get('email'),
                Phone_number=request.POST.get('number'),
                Password=request.POST.get('password'),
            )

            http_code_of_singup_api = 200
            signup_response_message = "Signup successful"

            return redirect('/')
        except Exception as e:
            http_code_of_singup_api = 400
            signup_response_message = str(e)
            return redirect('/')

    return JsonResponse({"error": "Only POST allowed"}, status=405)

# ---------------- LOGIN ---------------- #

@csrf_exempt
def login_api_view(request):
    global jwt_token, http_code_of_login_api, login_response_message, User, profile

    if request.method == 'POST':
        try:
            phone = request.POST.get('number')
            password = request.POST.get('password')

            user = Application_Users.objects.filter(
                Phone_number=phone,
                Password=password
            ).first()

            if user:
                jwt_token = "dummy_token"
                http_code_of_login_api = 200
                login_response_message = "Login successful"

                User = {
                    "Username": user.Username,
                    "Email": user.Email
                }

                profile = user.Username[0]

            else:
                http_code_of_login_api = 401
                login_response_message = "Invalid credentials"

            return redirect('/')

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Only POST allowed"}, status=405)

# ---------------- GET CITIES ---------------- #

def get_cities(request):
    data = place.objects.all()

    cities = []
    states = []

    for i in data:
        cities.append(i.cities)
        states.append(i.states)

    return {
        'cities': cities,
        'states': states,
    }

# ---------------- SEARCH ---------------- #

@csrf_exempt
def search_api_view(request):
    if request.method == 'POST':

        from_place = request.POST.get('from_place')
        to_place = request.POST.get('to_place')

        if(from_place == 'place' or to_place == 'place'):
            return redirect('/')

        try:
            results = search_bus_trips.objects.filter(
                from_place_id=from_place,
                to_place_id=to_place
            )

            CitiesList = get_cities(request)

            result_data = list(results.values())

            data = {
                'cities': CitiesList["cities"],
                'states': CitiesList["states"],
                'token': to_check_jwt(),
                'profile': profile,
                'search_results': result_data,
                'flag_and_language': flag_and_language,
            }

            return render(request, "search_bus_page.html", data)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Only POST allowed"}, status=405)

# ---------------- STATIC PAGES ---------------- #

def myprofile(request):
    return render(request, "myprofile.html", getdata())

def PrivacyAndPolicy(request):
    return render(request, "PrivacyAndPolicy.html", getdata())

def TermAndConditions(request):
    return render(request, "TermAndConditions.html", getdata())

def ContactUs(request):
    return render(request, "ContactUs.html", getdata())

def CancellationPolicy(request):
    return render(request, "CancellationPolicy.html", getdata())

def MyTickets(request):
    return render(request, "MyTickets.html", getdata())

def MyWallet(request):
    return render(request, "MyWallet.html", getdata())

def RefferAndEarn(request):
    return render(request, "RefferAndEarn.html", getdata())

# ---------------- LOGOUT ---------------- #

def Account_Logout(request):
    global token_exist, jwt_token, http_code_of_singup_api
    global http_code_of_login_api, login_response_message
    global User, profile, signup_response_message

    token_exist = False 
    jwt_token = None
    http_code_of_singup_api = 401
    http_code_of_login_api = 400
    login_response_message = None
    signup_response_message = None
    profile = ""
    User = {}

    return redirect("/")