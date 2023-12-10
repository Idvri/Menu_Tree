# UpTraderTest
Django App, которое реализовывает древовидное меню (рекурсия).

### Установка и запуск (локально):
- git clone https://github.com/Idvri/UpTraderTest.git;
- python -m venv venv;
- venv/Scripts/activate;
- pip3 install -r requirements.txt;
- python manage.py migrate;
- python manage.py runserver.

### Установка и запуск (Docker):
- docker-compose up --build - в первый раз;
- docker-compose up.

### Команды (локально):
- python manage.py csu - создать администратора. Логин и пароль: admin;
- python manage.py loaddata menu_data.json - наполнить БД данными из фикстур для основного меню;
- python manage.py loaddata menu_item_data.json - наполнить БД данными из фикстур для пунктов/подменю и подпунктов основного меню.

###### *Если запуск через Docker, то все команды будут выполнены автоматически.