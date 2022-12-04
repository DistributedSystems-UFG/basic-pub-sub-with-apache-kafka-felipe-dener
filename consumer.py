from kafka import KafkaConsumer
from const import *
import sys

consumer = KafkaConsumer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT],
                        auto_offset_reset='earliest',
                        enable_auto_commit='false')

topics_to_subscribe = []
print('type "none" to start follow your topics')
while True:
    topico = input('new topic:')
    if topico == 'none':
        break
    topics_to_subscribe.append(topico)

consumer.subscribe(topics_to_subscribe)

for msg in consumer:
    print(msg.value)
