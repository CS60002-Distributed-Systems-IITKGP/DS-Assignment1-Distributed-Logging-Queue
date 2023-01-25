import requests

class MyConsumer():
    def __init__(self, topics=[], broker):
        self.broker = broker
        self.subbedTopics = {}
        for topic in topics:
            self.__subscribe(topic)

    def get_next():
        pass

    def __subscribe(topic):
        url = self.broker + "/consumer/register"
        data = {
            "topic": topic
        }
        r = requests.post(url, data)
        if r.ok:
            res_body = r.json()
            

    # def __register():
        
        
        
        