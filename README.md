Проект каркас на Flask, Python 3.10, для вывода погоды,
используя API ресурса: https://www.weatherapi.com/
*******

Легко  масштабировать и изменить
*******

Основные возможности:
1. на главной странице есть форма ввода, для поиска города в локальной базе данных
2. После того как город найдет, будет выведена информация о погоде в данном городе
3. Есть автотесты(пока еще отлаживаются)

*******

В каталоге app - само приложение.
В файле test_app - автотесты.
База данных проекта - SQLite.
*******

Для запуска проекта: 
склонировать проект
Установить зависимости из файла requirements.txt. 
Запустить проект, используя файл run.py.
*******
Так же есть запуск проекта через Docker,(Пока еще в режиме отладки, контейнер создается, но не запускается)
*******
сборка
docker build -t app . 
*******
запуск
docker run -d -p 5000:5000 -e WEATHERAPI_KEY=3718ee97aa974c88aba43338252805 app
*******
проверка
http://localhost:5000



