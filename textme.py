from twilio.rest import Client
from fetch import *

client = Client()
numberDict = {}

for data in dataList:
    for number in numberDict.values():
        client.messages.create(
            to=[number],
            from_="",
            body=data
        )
