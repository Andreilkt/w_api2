import os
from dotenv import load_dotenv
from app import db
from app.models import City

# файл запуска проекта
load_dotenv()  # Загружает переменные окружения из файла .env
from app.app import app

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if City.query.count() == 0:
            cities = [
                City(name='Москва', lat=55.7558, lon=37.6173),
                City(name='Санкт-Петербург', lat=59.9343, lon=30.3351),
                City(name='Новосибирск', lat=55.0084, lon=82.9357),
                City(name='Екатеринбург', lat=56.8389, lon=60.6057),
                City(name='Казань', lat=55.7903, lon=49.1120),
            ]
            db.session.bulk_save_objects(cities)
            db.session.commit()

    app.run(debug=True)
