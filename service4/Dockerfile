FROM python:3.7

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .


ENTRYPOINT ["gunicorn" , "--workers=4", "--bind=0.0.0.0:5003", "app:app"]