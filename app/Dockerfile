FROM python:3.10

WORKDIR /usr/src/app

RUN pip install confluent-kafka

COPY main.py .

CMD ["python", "main.py"]
