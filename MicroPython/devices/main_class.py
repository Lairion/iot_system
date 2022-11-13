from sys import exit
from settings import HOSTNAME, CRED
from connector import Connector
from devices.diod import Diod
from devices.servo import ServoItem


class Device:

    items_classes = {
        "diod": Diod,
        "servo": ServoItem
    }

    def __init__(self, device_id, host_name, cred):
        self.device_id = device_id
        self.connector = Connector(host_name, cred)
        self.connector.auth()
        response = self.connector.get("devices", str(self.device_id))
        if not response:
            print("Can`t get data")
            exit(1)
        json = response.json()
        items = json["items"]
        if not items:
            print("Device didn't have items")
            exit(1)
        print(json)
        for item in items:
            print(item)
            name = item["item"]["name"]
            print(name)
            item_class = self.items_classes.get(name, False)
            if not item_class:
                f"{name} item not implemented"
                continue
            item_dict = {
                "connector": self.connector,
                "id": item["id"],
                "name": name,
                "pins": item["pins"],
                "on": item["on"]
            }
            setattr(self, f"{name}_{item['id']}", item_class(**item_dict))

    def get_task(self):
        print("Get data")
        response = self.connector.get(
            "devices", str(self.device_id), "task"
        )
        if not response:
            return False
        self.data = response.json()
        print(self.data)
        response.close()
        return self.data["status"]["name"]

    def update_items(self):
        items_for_change = self.data["items_in_tasks"]
        for i in items_for_change:
            name = i["item"]["name"]
            atr = getattr(self, f"{name}_{i['device_item']}", False)
            if atr:
                atr.fresh_status(bool(i["on"]))
            print("Skiped:", name)

    def close_status(self):
        response = self.connector.patch(
            "device_tasks",
            str(self.data["id"]),
            "change_status",
            name="COMPLETE"
        )
        print(response.text)
        if response:
            response.close()

    def make_action_by_data(self):
        self.update_items()
        self.close_status()
