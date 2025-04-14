import requests
from django.conf import settings


def get_external_data():
    url = 'http://127.0.0.1:8000/api/v1/users/'
    headers = {'Authorization': 'Bearer YOUR_TOKEN_HERE'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None
    

    
def post_to_external_api(request):
    url = 'http://127.0.0.1:8000/api/v1/users/'
    headers = {'Authorization': 'Bearer YOUR_TOKEN_HERE',
               'Content-Type': 'application/json',}
    
    try:
        response = requests.post(url,json=request, headers=headers)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"POST request failed: {e}")
        return None