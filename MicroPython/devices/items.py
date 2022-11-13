class Item:

    def __init__(self, connector, id, name, on):
        self.connector = connector
        self.id = id
        self.name = name
        self.fresh_status(on)

    def fress_status(self, status):
        pass

    def on_status(self, status):
        on_dict = {"on": status}
        self.connector.patch("device_items", str(self.id), **on_dict)
