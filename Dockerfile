FROM python:3.12

WORKDIR /app

COPY src src
COPY config config
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "src/main.py"]