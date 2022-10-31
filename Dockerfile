FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
ENV DOCKER=True
RUN mkdir /app_grupo3
RUN mkdir /data
WORKDIR /app_grupo3
COPY requirements.txt /app_grupo3/
RUN pip install -r requirements.txt
COPY . /app_grupo3/
RUN python englishwebsite/manage.py makemigrations
RUN python englishwebsite/manage.py migrate
RUN python englishwebsite/manage.py rebuild_index --noinput

CMD python englishwebsite/manage.py makemigrations;python englishwebsite/manage.py migrate;python englishwebsite/manage.py runserver 0.0.0.0:8000