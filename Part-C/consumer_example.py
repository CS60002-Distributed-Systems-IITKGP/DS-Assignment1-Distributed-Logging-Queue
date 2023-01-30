from distributed_queue_sdk.consumer import MyConsumer

try:
    consumer = MyConsumer(
        broker="http://localhost:8000", topics=["abc", "xyz"])
    consumer.get_next("abc")
except Exception as error:
    print(error)
