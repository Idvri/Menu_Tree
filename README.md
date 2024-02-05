# UpTraderTest
Django App, которое реализовывает древовидное меню (рекурсия).

### Stack: 
- Python 3.11;
- Django 5.0;
- SQLite;
- Docker (опционально).

### Установка и запуск (локально):
- git clone https://github.com/Idvri/UpTraderTest.git;
- python -m venv venv (находясь в папке проекта);
- venv/Scripts/activate (Windows);
- source venv/bin/activate (Linux);
- pip3 install -r requirements.txt;
- python manage.py migrate;
- python manage.py runserver.

### Установка и запуск (Docker):
- docker-compose up --build - в первый раз;
- docker-compose up.

### Доступность (адреса):
- 127.0.0.1:8000;
- localhost:8000.

### Команды (локально):
###### Если запуск через Docker, то все команды будут выполнены автоматически.
- python manage.py csu - создать администратора. Логин и пароль: admin;
- python manage.py loaddata menu_data.json - наполнить БД данными из фикстур для основного меню;
- python manage.py loaddata menu_item_data.json - наполнить БД данными из фикстур для пунктов/подменю и подпунктов основного меню.
###### Внимание!!! Фикстуры сделаны абсолютно рандомно для того, чтобы с ними можно было поиграться. К примеру, пунктом в подменю "Чай" может быть "Лимонад" и это будет не ошибка, так как такая связь была установлена в админке. Вы можете самостоятельно распределить логику вашего меню, вырисовываться будет в зависимости от того, как именно вы настроили связи.

### Функционал:
- создание меню, пунктов и подпунктов в стандартной админ панели;
- отображение меню, пунктов и подпунктов в древовидном варианте.

