import paho.mqtt.client as mqtt

def mqtt_client_initialise():
    client = mqtt.Client("subscriber2")
    client.on_connect = mqtt_broker_on_connect
    client.on_message = mqtt_broker_on_message
    client.on_disconnect = mqtt_broker_on_disconnect
    #client.username_pw_set("guest","guest")
    return client

def mqtt_broker_on_connect(client, userdata, flags, rc):
    print("Connected with result code"+str(rc))
    if(rc != mqtt.CONNACK_ACCEPTED):
        print("Error")
    #client.subscribe("house/bulbs/bulb1")

def mqtt_broker_on_message(client, userdata, msg):
    print(msg.topic+ " " +str(msg.payload))

def mqtt_connect(client, ip_addr):
    client.connect(ip_addr, 1883)
    #client.loop()
    client.subscribe("traffic/object/detections")

def mqtt_broker_on_disconnect(client, userdata, rc):
    print("Disconnected with result code"+str(rc))
    client.loop_stop()

def mqtt_publish(client, topic, objects):
    print("client: "+objects+":"+topic)
    client.publish(topic, objects)

def establish_connection(ip_addr):
    mqtt_client = mqtt_client_initialise()
    #mqtt_client.loop_start()
    mqtt_connect(mqtt_client, ip_addr)
    return mqtt_client

#Code to test mqtt_ops
mqtt_client = establish_connection("192.168.0.105")
#mqtt_client.connect("192.168.0.107")
mqtt_client.loop_forever()
