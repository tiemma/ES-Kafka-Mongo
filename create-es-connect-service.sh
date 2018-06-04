#!/bin/sh

sleep 10

# Create sink service for ES using Kafka Connect endpoint
curl -X POST http://kafka-connect:8083/connectors/ -H "Content-Type: application/json" -d '{
  "name": "gritServer",
  "config": {
    "connector.class": "io.confluent.connect.elasticsearch.ElasticsearchSinkConnector",
    "tasks.max": "1",
    "topics": "gritServer",
    "key.ignore": "true",
    "schema.ignore": "true",
    "connection.url": "http://elasticsearch:9200",
    "type.name": "json",
    "name": "ES-Sink"
  }
}';