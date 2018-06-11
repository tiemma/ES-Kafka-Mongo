#!/usr/bin/env python3
from confluent_kafka.avro import CachedSchemaRegistryClient as SchemaRegistry
from simulator.producer import SimProducer
from simulator.manager import DeviceSimulator
from simulator.register_schema import RegisterSchema

schema_subject = 'meter_data_stream_v0'
schema_registry = 'http://schema-registry:8081'
schema_file = 'stream.avsc'
topic = 'grits_v1'
group_id = 'test01'

a, b, _ = SchemaRegistry(schema_registry).get_latest_schema(schema_subject)
print(a)
if b is None:
    register_schema = RegisterSchema(schema_registry, subject=schema_subject, file=schema_file)
    register_schema.post_schema()
    print('Registered schema at {} with subject {}\n'.format(schema_registry, schema_subject))
else:
    print('Schema registered at {} with subject {}\n'.format(schema_registry, schema_subject))

producer = SimProducer(
    bootstrap_servers='kafka',
    schema_registry=schema_registry,
    group_id=group_id,
    topic=topic,
    schema_subject=schema_subject
)
simulator = DeviceSimulator(producer=producer)
simulator.sim_device_messages()
