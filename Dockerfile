FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt

COPY ./app /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=80"]