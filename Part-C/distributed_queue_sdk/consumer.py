import requests


class MyConsumer():
    def __init__(self, broker, topics=[]):
        self.broker = broker
        self.subbedTopics = {}
        for topic in topics:
            self.__subscribe(topic)

    def __subscribe(self, topic_name):
        url = self.broker + f'/consumer/register'
        body = {"topic": topic_name}
        response = requests.post(url, json=body)
        res_json = response.json()
        if response.status_code == 404:
            # print(f'Failed to subscibbed to {topic_name} : Topic not found')
            print(res_json["detail"]["message"])
        elif response.status_code == 201:
            consumer_id = res_json["consumer_id"]
            self.subbedTopics[topic_name] = consumer_id
            # print(f'Consumer {consumer_id} subscribbed to {topic_name}')
            raise Exception(
                f'Consumer {consumer_id} subscribbed to {topic_name}')

    def get_next(self, topic_name):
        if topic_name not in self.subbedTopics:
            print(f'Not subscribed to the topic : {topic_name}')
        else:
            consumer_id = self.subbedTopics[topic_name]
            print(consumer_id)
            self.__recvMsg(topic_name, consumer_id)
            # msg = self.__recvMsg(topic_name, consumer_id)
            # if msg:
            #     print(f'New message in {topic_name} : {msg}')
            # else:
            #     print(f'No new message in this topic!')

    def __recvMsg(self, topic_name, consumer_id):
        url = self.broker + '/consumer/consume'
        body = {
            "topic": topic_name,
            "consumer_id": consumer_id
        }
        response = requests.get(url, json=body)
        res_json = response.json()
        if response.status_code == 404:
            print(res_json["detail"]["message"])
        if response.status_code == 200:
            print(res_json["message"])
