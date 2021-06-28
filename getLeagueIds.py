import xml.etree.ElementTree as ET
import requests
from tokenA import token_auth

donbest = ET.fromstring(requests.get(
    'http://xml.donbest.com/v2/league/?token='+token_auth).text)

leagueDict = {}
sportDict = {}
leagueSportDict = {}

for line in donbest:
    if line.tag == 'league':
        leagueId = line.attrib['id']
        for element in line:
            if element.tag == 'name':
                leagueName = element.text
            elif element.tag == 'sport':
                sportId = element.attrib['id']
                for ele in element:
                    if ele.tag == 'name':
                        sportName = ele.text
        leagueSportDict[leagueId] = sportName
        leagueDict[leagueId] = leagueName
        sportDict[sportId] = sportName
    else:
        continue
