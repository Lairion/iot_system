from machine import Pin
from devices.items import Item


class Diod(Item):

    def __init__(self, connector, id, name, pins, on):
        list_of_pins = pins.replace(", ", ",").split(",")
        self.pin = Pin(int(list_of_pins[0]), Pin.OUT)
        super().__init__(connector, id, name, on)

    def fresh_status(self, status):
        if status:
            self.pin.on()
            return None
        self.pin.off()
