import requests
from django.conf import settings

# api consumer of the login api sending the response of the user data
def post_login_data(request):
    url = 'http://127.0.0.1:8000/api/v1/login/'
    headers = {'Authorization': 'Bearer YOUR_TOKEN_HERE',
               'Content-Type': 'application/json',}
    
    try:
        response = requests.post(url,json=request, headers=headers)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"POST request failed: {e}")
        return None
    

# api sending the response as the user saved in the Application_Users model 
def post_to_signup_api(request):
    url = 'http://127.0.0.1:8000/api/v1/users/'
    headers = {'Content-Type': 'application/json',}
    
    try:
        response = requests.post(url,json=request, headers=headers)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"POST request failed: {e}")
        return None