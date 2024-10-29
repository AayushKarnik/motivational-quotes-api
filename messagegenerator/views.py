import requests
from django.http import JsonResponse

def home(request):
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        data = response.json()[0]
        return JsonResponse({'quote': data['q'], 'author': data['a']})
    return JsonResponse({'error': 'Unable to fetch a message at the moment.'})
