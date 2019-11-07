from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from .models import City


# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=092520fee78b132459dd966f339e2215'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    cities = City.objects.all()

    form = CityForm()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city.name)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/weather.html', context)