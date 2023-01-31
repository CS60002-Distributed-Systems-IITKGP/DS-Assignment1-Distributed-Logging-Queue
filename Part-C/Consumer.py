import requests

class MyConsumer():
    def __init__(self, broker, topics=[]):
        self.broker = broker
        self.subbedTopics = {}
        for topic in topics:
            self.__subscribe(topic)

    def get_next(topic_name):
        if topic_name not in self.subbedTopics:
            print(f'Not subscribed to the topic : {topic_name}')
        else:
            consumer_id = self.subbedTopics[topic_name]
            msg = self.__recvMsg(topic_name, consumer_id)
            # if msg:
            #     print(f'New message in {topic_name} : {msg}')
            #     return msg
            # else:
            #     print(f'No new message in this topic!')
            #     return None
            return msg

    def __subscribe(topic_name):
        url = self.broker + f'/consumer/register/{topic_name}'
        response = requests.post(url)
        if response.status_code == 404:
            print(f'Failed to subscibbed to {topic_name} : Topic not found')
        elif response.status_code == 201:
            response_body = r.json()
            consumer_id = response_body["consumer_id"]
            self.subbedTopics[topic_name] = consumer_id
            print(f'Consumer {consumer_id} subscribbed to {topic_name}')

    def __recvMsg(topic_name, consumer_id):
        url = self.broker + f'/consumer/consume/{topic_name}/{consumer_id}'
        response = requests.get(url)
        if response.status_code == 404:
            return None
        if response.status_code == 200:
            return r.json()
            
    
    
    # def __register():
        
        
        
        