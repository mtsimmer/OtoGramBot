#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""General Notes


Regarding the resource_ID
registerd car numbers: 053cea08-09bc-40ec-8f7a-156f0677aff3
diregisterd cars: 851ecab1-0622-4dbe-a6c7-f950cf82abf9 
self import: 03adc637-b6fe-402b-9937-7c3d3afc9140
MobileEye priceOff: 83bfb278-7be1-4dab-ae2d-40125a923da1


##Maybe Usefull for further implamintation
licensed resellers: eb74ad8c-ffcd-43bb-949c-2244fc8a8651
statistics regarding models on the market: 5e87a7a1-2f6f-41c1-8aec-7216d52a6cf6 
Recalls: 

"""

import requests
import json
from config import *

CURR_OFFSET = "0"

def main():
    #print(query_apis("9489419")[0]['success']) #Simple Check weather the first api was good
    #print(query_apis("9489419")[1]['success'])
    #print(query_apis("9489419")[2]['success'])
    #print(query_apis("9489419")[3]['success'])
    tele_reply("Hi","824323813")
    while True:
        get_updates()


def _query_apis(q):
    replies = [] #list of the returned jsons (a list of dicts)
    for resource_id in RESOURCE_IDS:
        url = GENERIC_URL + resource_id
        data = GENERIC_DATA
        data['resource_id'] = resource_id
        data['q'] = q
        raw_reply = requests.request(REQUEST_TYPE,url,data=data)
#        raw_reply = raw_reply.decode("utf-8")
        replies.append(json.loads(raw_reply.text))
    return replies


def tele_reply(reply, chat_id):
    url = GENERIC_TELEGRAM_API + TELEGRAM_BOT_TOKEN + "/sendMessage"
    data = {"chat_id" : chat_id,
            "text" : reply}
    print("=============The message that sent:" + reply) #DEBUG
    sent = requests.request("POST",url,data=data)
    print(sent.text) #DEBUG

def get_updates():
    print(CURR_OFFSET) #DEBUG
    url = GENERIC_TELEGRAM_API + TELEGRAM_BOT_TOKEN + "/getUpdates" + "?offset=" + CURR_OFFSET + "?timeout=100"
    updates = requests.request("GET",url)
    _parse_update(json.loads(updates.text))

def _parse_update(raw_reply):
    updates = raw_reply["result"]
    if updates: #Pretty much always true.
        for req in updates:
            global CURR_OFFSET 
            CURR_OFFSET = str(req["update_id"]+1)
            print(CURR_OFFSET) #DEBUG
            try:
                car_num = req["message"]["text"]
            except:
                car_num = None
            chat_id = req["message"]["from"]["id"] #Supposed to be present otherwise there wont be an update.
        print("the message from the user:" + car_num) #DEBUG
        reply = compose_message(car_num, chat_id)
        #tele_reply(reply,chat_id)


def compose_message(car_num, chat_id):
    if car_num.isdigit():
        if len(car_num) > 6:
            api_replies = _query_apis(car_num)
            for api_reply in api_replies:
                composed_message = json.dumps(api_reply["result"]["records"],indent=2,ensure_ascii=False)
                print(composed_message) #DEBUG
                tele_reply(composed_message,chat_id)
    else:
        tele_reply("Invalid Input",chat_id)

def check_recall():
    pass
    
    

if __name__ == '__main__':
    main()

