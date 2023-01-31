from Consumer import MyConsumer

consumer = MyConsumer(broker = "localhost:8000", topics = ["abc", "xyz"])
msg = consumer.get_next("abc")
print(msg)