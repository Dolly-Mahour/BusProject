from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import  date, datetime, time , timedelta
import requests
# from .api_consumer import register_user
from .api_consumer import post_to_signup_api,post_login_data,get_from_place_api  #,verify_token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages

def get_cities(request):
    data = cities_api_view(request)
    # print(type(data.content))
    decoded_data = data.content.decode('utf-8')
    places = data.content
    parsed_json = json.loads(decoded_data)

    cities =[]
    states =[]
    combined =[]
    for i in parsed_json:
        cities.append(i["cities"])
        states.append(i["states"])
    
    combined.append(cities+states)
    print(len(cities))
    size = len(cities)
    combined_list = zip(cities,states)
    context = {
        'cities' : cities,
        'states' : states,
        'combined_list' : combined_list,
        # 'range' : range(size)
    }
    return context


def homepage(request):
    context = get_cities(request)
    return render(request,"busify.html",context)

@csrf_exempt
def signup_api_view(request):
    if request.method == 'POST':
        print(request.body)
        try:
            data ={
                "Username": request.POST.get('username'),
                "User_or_Agent": True,
                "Email": request.POST.get('email'),
                "Phone_number": request.POST.get('number'),
                "Password": request.POST.get('password'),
                "Referral_code": request.POST.get('ref-code')
            }
            print(data)
            # result is getting all the details of the user created
            result = post_to_signup_api(data)
            # print("this  is the result ---------",result)
            # if result["status"] == 200 :
            #   messages.success(request,"User created successfully")
            # else :
            #   messages.success(request,"User exists")
            # print("this is the",result)
            print(result)
            return JsonResponse(result or {"error": "Invalid JSON"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    

    return JsonResponse({"error": "Only POST allowed"}, status=405)



@csrf_exempt
def login_api_view(request):
    if request.method == 'POST':
        print(request.body)
        try:
            data ={
                "Phone_number": request.POST.get('number'),
                "Password": request.POST.get('password'),
            }
            result = post_login_data(data)
            if result["status"] == 200 :
                jwt_token = result["token"]
                request.session["jwt_token"] = jwt_token
                print("session token ---------------",request.session["jwt_token"])
                context = get_cities(request)
                # print(context["cities"])
                # data={
                #     'cities' : context["cities"],
                #     'states' : context["states"],
                # }
            # return JsonResponse(result or {"error": "API call failed"}, safe=False)
                return redirect('homepage')
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    

    return JsonResponse({"error": "Only POST allowed"}, status=405)





@csrf_exempt
def cities_api_view(request):
    # if request.method == 'POST':
        print(request.body)
        try:
            result = get_from_place_api()
            return JsonResponse(result or {"error": "API call failed"}, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)