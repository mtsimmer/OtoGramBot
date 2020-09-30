"""General Info

This file contains all of the consts of the bot
"""

"""
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

RESOURCE_IDS = ["053cea08-09bc-40ec-8f7a-156f0677aff3","851ecab1-0622-4dbe-a6c7-f950cf82abf9","03adc637-b6fe-402b-9937-7c3d3afc9140","83bfb278-7be1-4dab-ae2d-40125a923da1"]
GENERIC_URL = "https://data.gov.il/api/3/action/datastore_search?resource_id="
GENERIC_DATA = {'resource_id':None, #Contained in the url, depends on what API we are requesting
                'limit':1, #lmits the amount of answers.
                'q':None} #The Query (Pretty much what the user provides).
REQUEST_TYPE = "POST"

#Make sure to remove before commit.
TELEGRAM_BOT_TOKEN = ""

GENERIC_TELEGRAM_API = "https://api.telegram.org/bot"
INITIAL_OFFSET = "1"
