import pytest
from app import db
from config import Config
from app.app import app, City


@pytest.fixture
def client():
    # Настройка тестового клиента Flask и базы в памяти
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Добавляем тестовые города
            cities = [
                City(name='Москва', lat=55.7558, lon=37.6173),
                City(name='ТестовыйГород', lat=0, lon=0),
            ]
            db.session.bulk_save_objects(cities)
            db.session.commit()
        yield client
        # После тестов очищаем базу
        with app.app_context():
            db.session.remove()
            db.drop_all()


def test_index_get(client):
    """Проверка загрузки главной страницы GET"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Введите название города' in response.data


def test_post_existing_city(client):
    """Отправка POST с существующим городом"""
    response = client.post('/', data={'city': 'Москва'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Погода' in response.data
    assert b'\xc2\xb0C' in response.data  # символ °C в utf-8


def test_post_nonexistent_city(client):
    """Отправка POST с несуществующим городом"""
    response = client.post('/', data={'city': 'Город_Которого_Нет'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'не найден в базе' in response.data


def test_post_empty_city(client):
    """Отправка POST с пустым значением"""
    response = client.post('/', data={'city': ''}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Введите название города' in response.data
