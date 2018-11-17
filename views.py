import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d21022e1c74eb73c45cf5e1958865487'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()
    weather_data = []

    for city in cities:
        response = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],

        }

        weather_data.append(city_weather)

    context = {'city_weather' : weather_data,'form':form}

    # print(context)



    return render(request,'weather/weather.html', context)
