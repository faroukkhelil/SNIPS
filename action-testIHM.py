# !/usr/bin/env python
# encoding: utf-8
import paho.mqtt.client as mqtt
import json
import webbrowser

def on_connect(client, userdata, flags, rc):
    print('Connected')
    mqtt.subscribe('hermes/intent/#')
def on_message(client, userdata, msg):
    
    url="http://www.google.fr/"
    intent_json = json.loads(msg.payload)
    intentName = intent_json['intent']['intentName']
    slots = intent_json['slots']
    #print('Intent {}'.format(intentName))
    opt=""
    for slot in slots:
        slot_name = slot['slotName']
        raw_value = slot['rawValue']
        value = slot['value']['value']
        if slot_name == "ref_num" or slot_name == "numero_devis" :
                value = str(int(float(value)))
        if opt == "" :
                opt=slot_name+"="+value
        else :
                opt=opt+"&"+slot_name+"="+value
    if "client" in intentName :
      url = "https://atlas-2c.rec.sgdbf.saint-gobain.net:8022/#/customer/"+opt
    if "devis" in intentName :
      url = "https://atlas-2c.rec.sgdbf.saint-gobain.net:8022/#/document/order/"+opt+"/view/basket"
    webbrowser.open(url+, new=2)

mqtt = mqtt.Client()
mqtt.on_connect = on_connect
mqtt.on_message = on_message
mqtt.connect('raspberrypi.local', 1883)
mqtt.loop_forever()
