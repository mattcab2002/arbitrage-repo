from twilio.rest import Client
from fetch import *

client = Client("AC2acc8091156130d1852c67bcfb173db4",
                "22927d59f4caa89f9eaa723c4d933209")
numberDict = {'Matthew Cabral': '15147437101'}

# 'Alex Kahan': '15149414428','Zach Kahan': '15148654428', 'Dylan Hacker': '15148940337', 'Max Kadanoff': '15145026295'

# 'Evan Stern':'15149415566','Aidan Bienstock':'15144025344','AJ Titleman':'15142426888','Oren Arbel-Wood':'15145195547'

for data in dataList:
    for number in numberDict.values():
        client.messages.create(
            to=[number],
            from_="+12724358138",
            body=data
        )
