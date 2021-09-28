FROM python:3.9.0

WORKDIR /home/

RUN echo "a-5"

RUN git clone https://github.com/go-tech01/gis_4ban_1.git

WORKDIR /home/gis_4ban_1/

#RUN echo "SECRET_KEY=django-insecure-)yo2fo5n7^c&17y0g#4!8q4-ns=-0qm@j2(7gl3ra7dfm1&_mz" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=gis_4ban_1.settings.deploy && python manage.py migrate --settings=gis_4ban_1.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=gis_4ban_1.settings.deploy gis_4ban_1.wsgi --bind 0.0.0.0:8000"]
