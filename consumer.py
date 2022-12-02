from kafka import KafkaConsumer
from const import *
import sys

consumer = KafkaConsumer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT],
                        auto_offset_reset='earliest',
                        enable_auto_commit='false');


consumer.subscribe(['Health'])

for msg in consumer:
    print (msg.value)
