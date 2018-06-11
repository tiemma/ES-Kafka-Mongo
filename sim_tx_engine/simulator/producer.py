from time import sleep, time
from confluent_kafka.avro import AvroProducer
from confluent_kafka.avro import CachedSchemaRegistryClient as SchemaRegistry, MessageSerializer
from random import randrange
import arrow
from simulator.full_messages import device_message


class Producer(object):
    """docstring for Producer"""

    def __init__(self, bootstrap_servers=None, schema_registry=None, group_id=None, topic=None, schema_subject=None):
        super(Producer, self).__init__()
        self.bootstrap_servers = bootstrap_servers
        self.schema_registry = schema_registry
        self.group_id = group_id
        self.topic = topic
        self.schema_subject = schema_subject
        self.avro_producer = AvroProducer({
            'bootstrap.servers': self.bootstrap_servers,
            'schema.registry.url': self.schema_registry,
        },
            default_value_schema=self.value_schema)

    @property
    def value_schema(self):
        if self.schema_subject is None or self.schema_registry is None:
            raise ValueError('Schema subject AND schema_registry required')
        _, schema, _ = SchemaRegistry(self.schema_registry).get_latest_schema(self.schema_subject)
        return schema

    def send_message(self, message):
        if not(message):
            raise ValueError("Message is required")

        self.avro_producer.produce(topic=self.topic, value=message)
        self.avro_producer.flush()


class SimProducer(Producer):
    """Inherits Kafka producer class"""

    def __init__(self, bootstrap_servers, schema_registry, group_id, topic, schema_subject):
        Producer.__init__(self, bootstrap_servers, schema_registry, group_id, topic, schema_subject)
        self.bootstrap_servers = bootstrap_servers
        self.schema_registry = schema_registry
        self.group_id = group_id
        self.topic = topic
        self.schema_subject = schema_subject
        self.schema_id = SchemaRegistry(self.schema_registry).get_latest_schema(self.schema_subject)[0]
        self.serializer = MessageSerializer(SchemaRegistry(self.schema_registry))

    def produce_one_message(self, message):
        """Dev Function"""
        self.send_message(message)

    def produce_forever(self, message_func):
        """Dev Function"""
        t1 = time()
        count = 1
        while True:
            current_time = str(arrow.now('Africa/Lagos').format("YYYY-MM-DDTHH:mm:ss.SSSZZ"))
            # from pytz import timezone
            # from datetime import datetime
            # tz = timezone('Africa/Lagos')
            # xm = tz.localize(datetime.now()).strftime('%Y-%m-%dT%H:%M:%S.%f%z')
            # current_time = "".join((xm[0:23], xm[26:31]))
            message = device_message(current_time)
            #print(message)
            print('\nMessage count = {}'.format(count))
            print('Topic: {}'.format(self.topic))
            print('Subject: {}'.format(self.schema_subject))
            print('Duration (Seconds): {} seconds'.format(time() - t1))
            print('Duration (Minutes): {} minutes'.format((time() - t1) / 60))
            print('Velocity {} messages per second'.format(count / (time() - t1)))
            print('Velocity {} messages per minute'.format(count / ((time() - t1) / 60)))
            count += 1

            self.send_message(message)
            sleep(randrange(2, 4))
