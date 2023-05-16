import time
import datetime
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers = 'kafka:9092')

while True:
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = "Current time is " + str(current_time)
    producer.send('common', message.encode('utf-8'))
    print(f"Message sent: {message}")
    time.sleep(5)