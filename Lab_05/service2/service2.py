from kafka import KafkaConsumer

kafka_consumer = KafkaConsumer(
    'common', 
    bootstrap_servers='kafka:9092')

for message in kafka_consumer:
    print(f"Message received : {message.value.decode('utf-8')}")