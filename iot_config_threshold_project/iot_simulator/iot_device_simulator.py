import paho.mqtt.client as mqtt  # import the client1
import time
import json
from random import randint

QOS1 = 1
QOS2 = 1
CLEAN_SESSION = True
broker = "127.0.0.1"
MQTT_CREDENTIALS = {"user_name": "admin",
                    "password": "bkcloud"}
CONNECT_TIMEOUT = 3


class MqttSyncClient(mqtt.Client):
    def __init__(self, name, clean_session):
        mqtt.Client.__init__(self, name, clean_session=clean_session)
        self.username_pw_set(username=MQTT_CREDENTIALS['user_name'],
                             password=MQTT_CREDENTIALS['password'])
        self.on_message = self.on_message_handler
        self.on_connect = self.on_connect_handler
        self.on_publish = self.on_publish_handler
        self.on_disconnect = self.on_disconnect_handler
        self.is_connected = False

    def connect(self, host, port=1883, keepalive=60, bind_address=""):
        print("connecting to ", host)
        super(MqttSyncClient, self).connect(host)
        client.loop_start()
        time.sleep(CONNECT_TIMEOUT)
        if self.is_connected:
            print("Successful to connect to server " + host)
            return True
        else:
            print("Failed to connect to server " + host)
            return False

    def on_connect_handler(self, client, userdata, flags, rc):
        if rc == 0:
            self.is_connected = True
        print("Connected flags ", str(flags), "result code ", str(rc))

    @staticmethod
    def on_message_handler(client, userdata, message):
        print("message received  ", str(message.payload.decode("utf-8")))

    @staticmethod
    def on_publish_handler(client, userdata, mid):
        pass
        # print("message published ", str(message.payload.decode("utf-8")))

    @staticmethod
    def on_disconnect_handler(client, userdata, flags, rc=0):
        m = "DisConnected flags" + "result code " + str(rc)
        print(m)


if __name__ == "__main__":
    try:
        client = MqttSyncClient("iot_device_simulator",
                                clean_session=CLEAN_SESSION)
        connect_rs = client.connect(host='127.0.0.1', port=1883)
        if connect_rs is True:
            # publish message to MQTT broker
            base_temperature = 5
            # temperature mid range: 30, range 5-40
            base_humidity = 20
            # humidity mid range: 50, range 20 -100

            for i in range(1, 6):
                publish_data = {
                    'tem': base_temperature + randint(0, 35),
                    'humi': base_humidity + randint(0, 80)
                }
                ret = client.publish("icse/sensor", json.dumps(publish_data))
                time.sleep(5)
            client.loop_stop()
            client.disconnect()
        else:
            pass
            # client1.on_disconnect=on_disconnect
    except Exception as e:
        print e
