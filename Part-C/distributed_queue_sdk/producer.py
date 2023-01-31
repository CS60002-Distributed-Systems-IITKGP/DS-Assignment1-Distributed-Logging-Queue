import requests


class ProducerClient:
    # producer_id: str
    topics: list
    # topic: str
    broker_url: str
    subscribed_topics = {}

    def __init__(self, broker_url, topics):
        self.topics = topics
        self.broker_url = broker_url
        response = self.register_producer(topics, broker_url)
        # return response["message"]

    def register_producer(self, topics, broker_url):
        # http call using broker_url
        register_producer_url = broker_url + "/producer/register"
        for topic in topics:
            body = {"topic": topic}
            res = requests.post(register_producer_url, json=body)
            # set id
            res_json = res.json()
            # print(res_json)
            if res.status_code == 200:
                producer_id = res_json["producer_id"]
                # self.producer_id = producer_id
                self.subscribed_topics[topic] = producer_id
                print(
                    f"producer '{producer_id}' subscribed '{topic}' successfully")
                # return {"status_code": res.status_code, "message":}
            else:
                # return {"status_code": res.status_code, "message": res_json["message"]}
                # print(res_json["detail"])
                raise Exception(res_json["detail"])

    def send(self, topic, message):
        #Enqueue  /producer/produce
        enqueue_producer_url = self.broker_url + "/producer/produce"
        body = {
            "topic": topic,
            "producer_id": self.subscribed_topics[topic],
            "message": message
        }
        res = requests.post(enqueue_producer_url, json=body)
        res_json = res.json()
        if res.status_code == 200:
            # return {"status_code": res.status_code, "message": f"in {topic} \"{message}\" added successfully"}
            print(f"{topic} : \"{message}\" added successfully")
        else:
            # return {"status_code": res.status_code, "message": res_json["message"]}
            print(res_json["detail"])

    def can_send():
        # check is producer assigned to topic
        pass
