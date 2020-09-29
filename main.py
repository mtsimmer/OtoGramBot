import requests
import json

URLS = ["https://data.gov.il/api/3/action/datastore_search?resource_id=053cea08-09bc-40ec-8f7a-156f0677aff3"]
GENERIC_DATA = {'resource_id':None, #Contained in the url, depends on what API we are requesting
        'limit':1,  #limits the amount of answers
        'q':None} #The Query (Pretty much what the user provides)
REQUEST_TYPE = 'POST'

def main():
    #will be improved to run on multiple apis
    GENERIC_DATA['resource_id'] = '053cea08-09bc-40ec-8f7a-156f0677aff3'
    GENERIC_DATA['q'] = '6477751'
    reply = requests.request(REQUEST_TYPE,url=URLS[0],data=GENERIC_DATA)
    print(reply.text)

if __name__ == '__main__':
    main()

