import xml.etree.ElementTree as ET
import requests
from tokenA import token_auth

eventNamesDict = {}

donbest = ET.fromstring(requests.get(
    'http://xml.donbest.com/v2/schedule/?token='+token_auth).text)

for tag in donbest:
    if tag.tag == 'schedule':
        for sport in tag:
            for league in sport:
                for line in league:
                    if line.tag == 'group':
                        for event in line:
                            if event.tag == 'event':
                                id = event.attrib['id']
                                eventName = event.attrib['name']
                                eventNamesDict[id] = eventName
                            else:
                                continue
                    else:
                        continue
    else:
        continue
