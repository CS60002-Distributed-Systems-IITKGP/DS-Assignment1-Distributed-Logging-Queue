import time
from distributed_queue_sdk.producer import ProducerClient

try:
    producer = ProducerClient(
        broker_url="http://localhost:8000", topics=["abc", "xyz"])
    producer.send(topic="abc", message="log message 1")
    time.sleep(2)
    producer.send(topic="abc", message="log message 2")
    time.sleep(2)
    producer.send(topic="abc", message="log message 3")
    time.sleep(2)
    producer.send(topic="abc", message="log message 4")
except Exception as error:
    print(error)
