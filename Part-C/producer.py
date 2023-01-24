import requests


class ProducerClient:
    producer_id: str

    # topics: list
    topic: str
    broker_url: str

    def __init__(self, topic, broker_url):
        self.topic = topic
        response = self.register_producer(broker_url=broker_url)
        return response["message"]

    def register_producer(self, topic, broker_url):
        # http call using broker_url
        register_producer_url = broker_url + "/producer/register"
        # for topic in self.topics:
        #     res = requests.post(register_producer_url, data={"topic": topic})
        res = requests.post(register_producer_url, data={"topic": topic})
        # set id
        res_json = res.json()
        if res.status_code == 200:
            self.producer_id = res_json["producer_id"]
            return {"status_code": res.status_code, "message": f"{topic} subsribed successfully"}
        else:
            return {"status_code": res.status_code, "message": res_json["message"]}

    def send(self, topic, message):
        #Enqueue  /producer/produce
        enqueue_producer_url = self.broker_url + "/producer/produce"
        res = requests.post(enqueue_producer_url, data={
                            "topic": topic, "producer_id": self.producer_id, "message": message})
        res_json = res.json()
        if res.status_code == 200:
            return {"status_code": res.status_code, "message": f"in {topic} \"{message}\" added successfully"}
        else:
            return {"status_code": res.status_code, "message": res_json["message"]}

    def can_send():
        #
        pass
