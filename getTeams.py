import xml.etree.ElementTree as ET
import requests
from tokenA import token_auth

donbest = ET.fromstring(requests.get(
    'http://xml.donbest.com/v2/team/?token='+token_auth).text)

teamDict = {}

for line in donbest:
    if line.tag == 'sport':
        for element in line:
            if element.tag == 'league':
                for ele in element:
                    if ele.tag == 'team':
                        teamId = ele.attrib['id']
                        for el in ele:
                            if el.tag == 'full_name':
                                teamName = el.text
                            else:
                                continue
                        teamDict[teamId] = teamName
                    else:
                        continue
            else:
                continue
    else:
        continue
