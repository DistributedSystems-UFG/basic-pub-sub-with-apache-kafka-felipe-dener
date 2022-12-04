from kafka import KafkaProducer
from const import *

producer = KafkaProducer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT])

while True:
    topic = input("topico: ")
    msg = input("msg: ")
    producer.send(topic, value=msg.encode())
    producer.flush()
