import time
from machine import Pin, PWM
from devices.items import Item


class ServoItem(Item):

    def __init__(self, connector, id, name, pins, on):
        list_of_pins = pins.replace(", ", ",").split(",")
        self.servo = PWM(Pin(int(list_of_pins[0])), freq=50)
        self.servo.duty(0)
        super().__init__(connector, id, name, on)

    def fresh_status(self, status):
        print(status)
        if status:
            self.servo.duty(70)
            time.sleep(3)
            self.servo.duty(0)
            return None
        self.servo.duty(20)
        time.sleep(3)
        self.servo.duty(0)
