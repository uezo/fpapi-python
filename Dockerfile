FROM python:3.10.6-buster

RUN apt-get update

RUN mkdir -p /app
COPY ./src /app
COPY ./requirements.txt /app
WORKDIR /app

ENV PYTHONPATH=/app/src/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000"]
