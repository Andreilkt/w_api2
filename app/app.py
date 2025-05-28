from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
import requests

from app import app
from app.models import City

WEATHERAPI_KEY = '3718ee97aa974c88aba43338252805'


def get_weather(city_name):
    url = 'http://api.weatherapi.com/v1/forecast.json'
    params = {
        'key': WEATHERAPI_KEY,
        'q': city_name,
        'days': 1,  # Прогноз на 1 день
        'aqi': 'no',
        'alerts': 'no',
        'lang': 'ru'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print('Ошибка WeatherAPI:', response.status_code, response.text)
        return None


@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    city_name = ''
    if request.method == 'POST':
        city_name = request.form.get('city', '').strip()
        if not city_name:
            flash('Введите название города.')
        else:
            city = City.query.filter(City.name.ilike(city_name)).first()
            if not city:
                flash(f'Город "{city_name}" не найден в базе.')
            else:
                weather_data = get_weather(city.name)  # Передаем название города в WeatherAPI
                if not weather_data:
                    flash('Не удалось получить данные о погоде. Попробуйте позже.')
    return render_template('index.html', weather=weather_data, city=city_name)
