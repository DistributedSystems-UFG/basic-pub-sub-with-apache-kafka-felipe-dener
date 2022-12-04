from kafka import KafkaProducer
from const import *
import sys

topics = ['Health', 'Sports', 'Television']

producer = KafkaProducer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT])

for topic in topics:
    msg = topic + ' related message'
    print('Sending message about ' + topic + ': ' + msg)
    producer.send(topic, value=msg.encode())

producer.flush()
