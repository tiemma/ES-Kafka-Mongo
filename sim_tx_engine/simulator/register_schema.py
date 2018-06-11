from avro import schema
from confluent_kafka.avro import CachedSchemaRegistryClient as SchemaRegistry


class RegisterSchema(object):
    """Class for registering schema on kafka schema registry"""

    def __init__(self, url, subject, file):
        super(RegisterSchema, self).__init__()
        self.url = url
        self.subject = subject
        self.file = file
        self.avro_schema = self.from_schema_file()

    def from_schema_file(self):
        avro_file = open(self.file, "r+")
        schema_str = avro_file.read()
        avro_file.close()
        return schema.Parse(schema_str)

    def post_schema(self):
        schema_registry = SchemaRegistry(self.url)
        schema_registry.register(self.subject, self.avro_schema)

# register_schema = RegisterSchema('http://localhost:8081', 'meter_stream', 'stream.avsc')
# register_schema.post_schema()
# print(register_schema.url)
# print(register_schema.subject)

# print(SchemaRegistry('http://localhost:8081').get_latest_schema('meter_stream'))
# a, b, c = SchemaRegistry('http://localhost:8081').get_latest_schema('meter_stream')

# print(b.to_json())
