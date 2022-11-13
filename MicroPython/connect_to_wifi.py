import network


def do_wifi_connect(wifi_name, wifi_password):
    print("Start connection")
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(
            wifi_name,
            wifi_password
        )
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
