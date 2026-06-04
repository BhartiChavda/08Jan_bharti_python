import urllib.request
import urllib.parse
import json
import datetime
from django.shortcuts import render

def weather_view(request):
    weather_data = None
    forecast_data = None
    error_msg = None
    
    def get_weather_data(city_name):
        api_key = "93094dfa880ea9a8709e99c2bddc6334"
        
        # Current Weather
        url = f"https://api.openweathermap.org/data/2.5/weather?q={urllib.parse.quote(city_name)}&appid={api_key}&units=metric"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
        

        
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%I:%M %p')
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%I:%M %p')
        
        current = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': int(data['main']['temp']),
            'feels_like': int(data['main']['feels_like']),
            'temp_min': int(data['main']['temp_min']),
            'temp_max': int(data['main']['temp_max']),
            'pressure': data['main']['pressure'],
            'humidity': data['main']['humidity'],
            'visibility': data.get('visibility', 0) / 1000,
            'wind_speed': int(data['wind']['speed'] * 3.6), # m/s to km/h
            'wind_gust': int(data['wind'].get('gust', data['wind']['speed']) * 3.6),
            'wind_deg': data['wind'].get('deg', 0),
            'description': data['weather'][0]['description'].title(),
            'main_weather': data['weather'][0]['main'],
            'icon': data['weather'][0]['icon'],
            'sunrise': sunrise,
            'sunset': sunset,
            'date': datetime.datetime.now().strftime("%A, %d %B %Y"),
            'time': datetime.datetime.now().strftime("%I:%M %p")
        }
        
        return current

    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            try:
                weather_data = get_weather_data(city)
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    error_msg = f"City '{city}' not found. Please try again."
                else:
                    error_msg = "An error occurred with the API. Please try again."
            except Exception as e:
                error_msg = "An unexpected error occurred. Please try again."
    else:
        try:
            weather_data = get_weather_data("Rajkot")
        except:
            error_msg = "Failed to load default weather data."

    context = {
        'weather_data': weather_data if 'weather_data' in locals() else None,
        'error_msg': error_msg
    }
    return render(request, 'weather.html', context)
