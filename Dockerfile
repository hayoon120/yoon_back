FROM python:3.8.10

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /helloworld
WORKDIR /helloworld
COPY ./ ./

# RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential

EXPOSE 8000

CMD ["bash", "-c", "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"]