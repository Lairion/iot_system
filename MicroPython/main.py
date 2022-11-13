
import network
import time
import json
from devices.main_class import Device
from connect_to_wifi import do_wifi_connect

print("Start...")
print("Inited")


def main():
    file = open('config.json', 'r')
    config_json = json.loads(file.read())
    do_wifi_connect(
        config_json["wifi_name"],
        config_json["wifi_password"]
    )
    device = Device(
        1,
        config_json["hostname"],
        config_json["cred"]
    )
    while True:
        time.sleep(3)
        status = device.get_task()
        if status:
            device.make_action_by_data()


main()
print("Finish")
