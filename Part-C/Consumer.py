import requests
import threading
import time
import asyncio

class MyConsumer():
    def __init__(self, broker, topics=[]):
        self.broker = broker
        self.subbedTopics = {}
        for topic in topics:
            self.__subscribe(topic)

    async def get_next(self, topic_name):
        if topic_name not in self.subbedTopics:
            print(f'Not subscribed to the topic : {topic_name}')
        else:
            while True:
                consumer_id = self.subbedTopics[topic_name]
                msg = self.__recvMsg(topic_name, consumer_id)
                if msg:
                    print(f'New message in {topic_name} : {msg}')
                await asyncio.sleep(5)
                    # return msg
                # else:
                #     print(f'No new message in this topic!')
                    # return None
                
            # return msg

    def __subscribe(self, topic_name):
        url = f'http://{self.broker}/consumer/register/{topic_name}'
        response = requests.post(url)
        if response.status_code == 404:
            print(f'Failed to subscibe to {topic_name} : Topic not found')
        elif response.status_code == 201:
            response_body = response.json()
            consumer_id = response_body["consumer_id"]
            self.subbedTopics[topic_name] = consumer_id
            print(f'Consumer {consumer_id} subscribbed to {topic_name}')

    def __recvMsg(self, topic_name, consumer_id):
        url = f'http://{self.broker}/consumer/consume/{topic_name}/{consumer_id}'
        response = requests.get(url)
        if response.status_code == 404:
            return None
        if response.status_code == 200:
            return response.json()

    def size(self):
        url = f'http://{self.broker}/size/{topic_name}/{consumer_id}'
        response = requests.get(url)
        if response.status_code == 200:
            response_body = response.json()
            return int(response_body)
        
            
    
    
    # def __register():
        
        
        
        