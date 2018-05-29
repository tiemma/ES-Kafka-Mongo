# ES-Kafka-Mongo
Fully automated docker-compose setup for elasticsearch, zookeeper, kafka and mongoDB

- [Elasticsearch](http://elastic.co/)
- [Kafka](https://www.confluent.io/what-is-apache-kafka/)
- [MongoDB](https://www.mongodb.com/)
- [Zookeeper](https://zookeeper.apache.org/)

This docker-compose setup comes packed with the following configs:

#*All kafka services are from the confluent kafka stack*

 - Kafka Connect
 - Kafka Control Center
 - Elasticsearch 2.0
 - MongoDB
 - Zookeeper
 - Schema Registry
 - Kafka Rest
 
There are different service dependencies for each service 

You can run the docker-compose service by doing

> docker-compose up

Or run a specific service 

> docker-compose <service-name>

View all available services using

> docker-compose config --services
