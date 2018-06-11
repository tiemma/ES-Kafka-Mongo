from simulator.full_messages import device_message
from arrow import now


class DeviceSimulator():
    """docstring for Simulator"""

    def __init__(self, device_message_func=device_message, producer=None):
        super(DeviceSimulator, self).__init__()
        self.producer = producer
        self.device_message_func = device_message_func

    def device_message(self):
        return self.device_message_func(str(now()))

    def sim_device_messages(self):
        if self.producer is None:
            raise(ValueError('Producer not found'))
        message_func = self.device_message
        self.producer.produce_forever(message_func)
