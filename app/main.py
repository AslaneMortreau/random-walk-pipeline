from random import uniform
from time import sleep
from confluent_kafka import Producer
from json import dumps

def delivery_report(err, msg):
    if err is not None:
        print(f"An error occured: {err}")
    else:
        print(f'Message send to {msg.topic()} [{msg.partition()}]')

conf = {
    'bootstrap.servers': 'kafka1:9092',  
}

producer = Producer(conf)
prob = [0.33, 0.66]
walk = 0
while True:
    n = uniform(0, 1)
    if n < prob[0] : 
        walk-=1
    elif n > prob[1] :
        walk += 1 
    data = dumps({"walk" : walk})
    producer.produce('random_walk', data.encode('utf-8'), callback=delivery_report)
    producer.poll(0)
    sleep(5)