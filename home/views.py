from django.shortcuts import render,redirect
from datetime import  date, datetime, time , timedelta
import requests
# from .api_consumer import register_user
from .api_consumer import post_to_external_api
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def homepage(request):
    return render(request,"busify.html")

@csrf_exempt
def external_api_view(request):
    if request.method == 'POST':
        print(request.body)
        try:
            data ={
                "id": 1,
                "Username": request.POST.get('username'),
                "User_or_Agent": True,
                "Email": request.POST.get('email'),
                "Phone_number": request.POST.get('number'),
                "Password": request.POST.get('password'),
                "Referral_code": request.POST.get('ref-code')
            }
            print(data)
            result = post_to_external_api(data)
            return JsonResponse(result or {"error": "API call failed"}, safe=False)
        except json.JSONDecodeError:
            # data = json.loads(request.body)
            # print(request.body)
            # print(data)
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    

    return JsonResponse({"error": "Only POST allowed"}, status=405)