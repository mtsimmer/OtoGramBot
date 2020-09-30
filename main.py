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

def main():
    print(query_apis("9489419")[0]['success']) #Simple Check weather the first api was good
    print(query_apis("9489419")[1]['success'])
    print(query_apis("9489419")[2]['success'])
    print(query_apis("9489419")[3]['success'])
    


def query_apis(q):
    replies = [] #list of the returned jsons (a list of dicts)
    for resource_id in RESOURCE_IDS:
        url = GENERIC_URL + resource_id
        data = GENERIC_DATA
        data['resource_id'] = resource_id
        data['q'] = q
        raw_reply = requests.request(REQUEST_TYPE,url,data=data)
        replies.append(json.loads(raw_reply.text))
    return replies


def tele_reply(reply):
    url = ""
    pass



if __name__ == '__main__':
    main()

