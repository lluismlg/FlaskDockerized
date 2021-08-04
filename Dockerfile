FROM python:3.6-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn"  , "-b", "0.0.0.0:8080", "app:app"]
