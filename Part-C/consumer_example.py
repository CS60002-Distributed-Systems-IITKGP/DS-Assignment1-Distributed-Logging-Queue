import asyncio
from Consumer import MyConsumer

async def main():
    consumer = MyConsumer(broker = "localhost:8000", topics = ["abc", "xyz"])
    task1 = asyncio.create_task(consumer.get_next("abc"))
    task2 = asyncio.create_task(consumer.get_next("xyz"))
    await task1
    await task2

asyncio.run(main())
# consumer.get_next("xyz")