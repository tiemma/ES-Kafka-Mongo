#!/bin/sh

sleep 10;

# Create sink service for ES using Kafka Connect endpoint
curl -X POST http://kafka-connect:8083/connectors/ -H "Content-Type: application/json" -d '{
  "name": "grits_v1",
  "config": {
    "connector.class": "io.confluent.connect.elasticsearch.ElasticsearchSinkConnector",
    "tasks.max": "1",
    "topics": "grits_v1",
    "key.ignore": "true",
    "schema.ignore": "true",
    "connection.url": "http://elasticsearch:9200",
    "type.name": "json",
    "name": "ES-Sink"
  }
}';



sleep 20;


curl -X POST http://kafka-connect:8083/connectors/grits_v1/tasks/0/restart;

