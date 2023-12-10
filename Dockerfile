FROM python:3.11

WORKDIR /code/

COPY ./requirements.txt /code/
RUN pip install -r /code/requirements.txt
COPY . .
RUN touch db.sqlite3
RUN python manage.py migrate
RUN python manage.py csu
RUN python manage.py loaddata menu_data.json
RUN python manage.py loaddata menu_item_data.json