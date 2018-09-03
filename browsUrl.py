#!/usr/bin/env python2

import webbrowser
import sys

from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

def intent_received(hermes, intent_message):
    sentence = 'You asked for '

    if intent_message.intent.intent_name == 'fkhelil:demande_client':
        print('Demande de Fiche Client')
        sentence += 'Client '
        opt=''
        for i in range(2,len(sys.argv)) :
            if  i % 2 == 0 :
                opt=opt+sys.argv[i]+'='
            else :
                if i == len(sys.argv)-1 :
                    opt=opt+sys.argv[i]
                else :
                    opt=opt+sys.argv[i]+'&'
        url=sys.argv[1]
        webbrowser.open(url+'?'+opt, new=2)
    elif intent_message.intent.intent_name == 'fkhelil:demande_devis':
        print('Consultation de Devis')
        sentence += 'Devis '
    elif intent_message.intent.intent_name == 'fkhelil:demande_produit':
        print('Demande de Fiche Produit')
        sentence += 'Product '
    else:
        return

    forecast_country_slot = intent_message.slots.forecast_country.first()
    forecast_locality_slot = intent_message.slots.forecast_locality.first()
    forecast_start_datetime_slot = intent_message.slots.forecast_start_datetime

    if forecast_locality_slot is not None:
        sentence += 'in ' + forecast_locality_slot.value
    if forecast_country_slot is not None:
        sentence += 'in ' + forecast_country_slot.value
    if forecast_start_datetime_slot is not None and len(forecast_start_datetime_slot) > 0:
        sentence += ' ' + forecast_start_datetime_slot[0].raw_value

    hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
