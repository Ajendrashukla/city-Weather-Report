from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# OpenWeatherMap API key
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']

        # Make a request to the OpenWeatherMap API
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}
        response = requests.get(url).json()

        # Parse the response and extract the required data
        if response['cod'] == 200:
            weather_data = {
                'city': response['name'],
                'temperature': int(response['main']['temp']-273.15),
                'feels_like':int(response['main']['feels_like']-273.15),
                'temp_min':int(response['main']['temp_min']-273.15),
                'temp_max': int(response['main']['temp_max'] - 273.15),
                'humidity': response['main']['humidity'],
                'description': response['weather'][0]['description'],
                'complete':response
            }
        else:
            weather_data = None

        return render_template('weather.html', weather_data=weather_data)
    else:
        return render_template('weather.html', weather_data=None)


if __name__ == '__main__':
    app.run(debug=True)
