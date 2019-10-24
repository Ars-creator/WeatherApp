import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index (request):
    appid = 'b1b35bba8b434a28a0be2a3e1071ae5b&units=imperial'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

        all_cities.append(city_info)
    
    if (len(all_cities) > 5):
        all_cities.pop(0)
        City.objects.first().delete()
        

    context = {
        'all_info': all_cities,
        'form': form
    }

    return render(request, 'weather/index.html', context)