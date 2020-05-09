import requests
import json

def send_sms(message,number):

    url='https://www.fast2sms.com/dev/bulk'
    
    parameter={'authorization': '**************',#devoloper api key
               'sender_id':'FSTSMS',
               'message':message,
               'language':"english",
               'route':  "p",
               'numbers': number
               
              }
    response=requests.get(url,params=parameter)
    dictionary=response.json()
    print(dictionary)
    
send_sms('Hi vishal', '********')
