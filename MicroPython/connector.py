import urequests


class Connector:

    headers = {
        "Accept": "application/json",
        "content-type": "application/json",
        "Connection": "close"
    }

    def __init__(self, host_name, cred):
        self.host_name = host_name
        self.cred = cred

    def make_link(self, *args):
        list_for_link = [self.host_name]
        list_for_link += list(args)
        return "/".join(list_for_link) + "/"

    def post(self, *args, **kwargs):
        link = self.make_link(*args)
        try:
            response = urequests.post(link, json=kwargs, headers=self.headers)
        except Exception as e:
            return False
        return response

    def auth(self):
        response = self.post(
            "dj-rest-auth",
            "login",
            **self.cred
        )
        if not response:
            print("Not auth")
            return response
        print("connect")
        print(response.text)
        if response.status_code == 200:
            data = response.json()
            self.headers.update({
                "Authorization": f"Token {data['key']}"
            })
        response.close()

    def get(self, *args, **kwargs):
        print("Get...")
        args = list(args)
        if kwargs:
            param = '?' + "&".join([
                f"{k}={v}" for k, v in kwargs
            ])
            args.append(param)
        link = self.make_link(*args)
        print(link)
        try:
            response = urequests.get(link, headers=self.headers)
        except Exception as e:
            print("Connection issue")
            return False
        return response

    def patch(self, *args, **kwargs):
        print("Patch...")
        link = self.make_link(*args)
        print(link)
        print(self.headers)
        try:
            response = urequests.patch(link, json=kwargs, headers=self.headers)
        except Exception as e:
            print("Connection issue")
            return False
        return response
