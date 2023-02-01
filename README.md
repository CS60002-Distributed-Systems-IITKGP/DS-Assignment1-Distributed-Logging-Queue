<!-- **Distributed queue**

-   able to handle multiple producers and consumers that can subscribe to different topics
-   Different producers can publish topics asynchronously over the queue, whereas multiple consumers can retrieve the topics asynchronously, for which they are subscribed to -->

# Distributed Logging Queue
## Contributors
1. Suryawanshi Vivek Bapurao(coderviky) - 22CS60R62
2. Sairaj Das(sairajd044) - 22CS60R30
3. Sahil Mahapatra(dotslashbit) - 22CS60R14
4. Debdutta Mitra(Dmitra1993) - 22CS60R12
5. Sourajit Bhattacharjee(soura1819) - 22CS60R68


## Overview
Multiple producers subscribe to different topics and under those topics they generate log messages asynchronously and there are multiple consumers who are also subscribed to multiple topics and consumed those messages from the queue asynchronously.

## HTTP APIs
### Register Producer
This operation allows a producer to register for a certain topic with the message queue.For each subscription/registration of a specific topic, unique registration id will be assigned to the producer.If that specific topic is not present then it will create a new topic with the reqested topic name by calling **Create Topic API**.

```python
Method: POST
Endpoint: /producer/register
Params:
    "topic": <string>
Response:
    "status": <string>
    onSuccess:
        - "producer_id": <int>
    onFailure:
        - "message": "Connection failure" // Error message
```

### Create Topic
This operation allows to add a new topic to the list of available topics and producer as well as consumer are allowed to subscribe those topics.If that requested topic is already exists in DB, then "topic already exists!" error message will be generated.

```python
Method: POST
Endpoint: /topics
Params:
    - "name": <string>
Response:
    onSuccess:
        - "status": "success"
        - "message": <string>
    onFailure:
        - "status": "failure"
        - "message":  "topic already exists!" // error message
```

### List Topics
This operation returns all the available topics present in the queue.If no topics are available, then "no topics found!" error will be generated.
```python
Method: GET
Endpoint: /topics
Params:
    None
Response:
    "status": <string>
    onSuccess:
        - "topics": List[<string>] // List of topic names
    onFailure:
        - "message": "No topics found!" // Error message
``` 

### Register Consumer
This operation allows each consumer to register with a specific topic.A consumer can also register with multiple topics but for each topic registration, a unique registration id will be generated.If consumer tried to register with a topic which is not present in the queue, then error message "topic not found" will be generated.
```python
Method: POST
Endpoint: /consumer/register
Params:
    "topic": <string>
Response:
    "status": <string>
    onSuccess:
        - "consumer_id": <int>
    onFailure:
        - "message": "topic not found" // Error message
```

### Enqueue
This operation enlist a new log message produced by a particular producer of a particular topic producer subscribed. If producer is not subscribed to a topic which it is trying to add message, then "producer not found" error message will be generated else message will be added or appended to the corresponding topic queue.

```python
Method: POST
Endpoint: /producer/produce
Params:
    - "topic": <string>
    - "producer_id": <int>
        - "message": <string> // Log message to enqueue
Response:
    "status": <string>
    onSuccess:
        None
    onFailure:
        - "message": "Producer not found" // Error message
```

### Dequeue
This operation delist a log message from requested topic queue on FCFS basis.For a particular topic, as multiple consumers can be subscribed, so copy of the requested message of a topic will be forward to the consumer so that other consumer can also get the same message from the same topic, if it has been subscribed to.  
If consumer is not subscribed to a topic of which it is trying to get message, then "consumer not found" error message will be generated else message will be forward to the corresponding consumer.

```python
Method: GET
Endpoint: /consumer/consume
Params:
    - "topic": <string>
    - "consumer_id": <int>
Response:
    "status": <string>
    onSuccess:
        - "message": <string> // Log message
    onFailure:
        - "message": "Consumer not found" // Error message
```

### Size
This operation returns the number of messages still left to read for a particular topic of a consumer.If consumer requested to get the size of a topic which it is not subscribed, then "Consumer not found" error message will be generated.
```python
Method: GET
Endpoint: /size
Params:
    - "topic": <string>
    - "consumer_id": <int>
Response:
    "status": <string>
    onSuccess:
        - "size": <int>
    onFailure:
        - "message": "Consumer not found" // Error message
```
## Database Design
There are a total of 4 tables in the database:
1. Topic
2. Producer
3. Consumer
4. Message

### Topic
Topic table contains two attributes:
1. topic_id (primary key)
2. topic_name

### Producer
Topic table contains two attributes:
1. producer_id (primary key)
2. topic_id (foreign key)

### Consumer
Topic table contains two attributes:
1. consumer_id (primary key)
2. topic_id (foreign key)

### Message
Topic table contains three attributes:
1. message_id (primary key)
2. topic_id (foreign key)
3. message




## Tehcnology Used
1. Python3
2. FastAPI
3. Docker
4. PostgreSQL
5. git
6. Github

