import logging, random, time, re, sys, json
import paho.mqtt.client as mqtt

#logging.basicConfig(level = config.LOG_LEVEL)

class Publisher:
    def __init__(self, client_id, broker_ip = "192.168.0.105"):
        self.client = mqtt.Client(client_id = client_id)
        self.client.on_connect = self.on_connect
        self.client.on_disconect= self.on_disconnect
        self.client.on_publish = self.on_publish
        self.connected = False
        try:
            self.client.loop_start()
            self.client.connect(broker_ip, 1883)
        except:
            self.client.loop_stop()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected")
        if(rc == mqtt.CONNACK_ACCEPTED):
            self.connected = True
        else:
            self.connected = False
            print("Connection Failed")

    def on_disconnect(self, client, userdata, flags, rc):
        self.connected = False
        print("Lost connection")

    def on_publish(self, client, userdata, mid):
        pass

    def publish_value(self, topic, value):
        self.client.publish(topic, value, retain = True)


if __name__ == "__main__":
    try:
        random.seed()
        pub = Publisher(client_id = "producer1234", broker_ip = "192.168.0.105")
        while 1:
            read_value = random.randrange(15, 25, 1)
            pub.publish_value(read_value, "sample/topic")
            #time.sleep(2)
    except KeyboardInterrupt:
        print("Stopped By User")
    except:
        print("Other Error")
