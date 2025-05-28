import os

from app import app


# класс конфигурации проекта
class Config:
    app.config['TESTING'] = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'paraplan'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sities.db'  # Подключение к базе данных SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Отключение предупреждений о модификациях
