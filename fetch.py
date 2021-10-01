import xml.etree.ElementTree as ET
import requests
from functions import *
from getLeagueIds import *
from getTeams import teamDict
from sportsBooks import sportsBooksDict
from periodDescriptions import periodDict
from eventNames import eventNamesDict
from tokenA import token_auth
import time

todaysDate = str(time.strftime('%Y-%m-%d'))
dictOfEvents = {}
dataList = []

for key in leagueDict.keys():
    link = ('http://xml.url/' + key +
            '/?token='+token_auth, leagueSportDict[key])
    sport = link[1]
    league = leagueDict[key]
    try:
        donbest = ET.fromstring(requests.get(link[0]).text)
    except ET.ParseError:
        continue
    for event in donbest:  # all sportsbooks under the same event
        if event.tag == 'event':
            eventId = event.attrib['id']
        for line in event:
            awaySpread = awayPrice = homeSpread = homePrice = awayMoney = homeMoney = drawMoney = total = overPrice = underPrice = awayTotal = awayOverPrice = awayUnderPrice = homeTotal = homeOverPrice = homeUnderPrice = '0'
            # All Ids
            sportsBookId = line.attrib['sportsbook']
            periodAbb = line.attrib['period']
            if (line.attrib['type'] != 'previous') and (line.attrib['time'][:10] == todaysDate):
                for market in line:
                    if market.tag == 'ps':
                        awaySpread = float(market.attrib['away_spread'])
                        awayPrice = float(market.attrib['away_price'])
                        homeSpread = float(market.attrib['home_spread'])
                        homePrice = float(market.attrib['home_price'])
                    elif market.tag == 'money':
                        awayMoney = float(market.attrib['away_money'])
                        homeMoney = float(market.attrib['home_money'])
                        drawMoney = float(market.attrib['draw_money'])
                    elif market.tag == 'total':
                        total = float(market.attrib['total'])
                        overPrice = float(market.attrib['over_price'])
                        underPrice = float(market.attrib['under_price'])
                    elif market.tag == 'team_total':
                        awayTotal = float(market.attrib['away_total'])
                        awayOverPrice = float(market.attrib['away_over_price'])
                        awayUnderPrice = float(
                            market.attrib['away_under_price'])
                        homeTotal = float(market.attrib['home_total'])
                        homeOverPrice = float(market.attrib['home_over_price'])
                        homeUnderPrice = float(
                            market.attrib['home_under_price'])
                    else:
                        continue
                # Fetch data from dicts
                game = sportsBook = period = "NA"
                try:
                    game = eventNamesDict[eventId]
                    if game == 'OVER vs UNDER' or game == 'OVER RUNS VS UNDER RUNS':
                        continue
                    sportsBook = sportsBooksDict[sportsBookId]
                    period = periodDict[periodAbb]
                except KeyError:
                    continue
                # sport = sportDict
                # league = leagueDict
                name = sport+'-' + sportsBook + '-' + period + '-' + eventId + '-' + game + '.' + str(awaySpread) + '.' + str(awaySpread) + '.' + str(awayPrice) + '.' + str(homeSpread) + '.' + str(homePrice) + '.' + str(awayMoney) + '.' + \
                    str(homeMoney) + '.' + str(drawMoney) + '.' + str(total) + '.' + str(overPrice) + '.' + str(underPrice) + '.' + str(awayTotal) + '.' + \
                    str(awayOverPrice) + '.' + str(awayUnderPrice) + '.' + \
                    str(homeTotal) + '.' + str(homeOverPrice) + \
                    '.' + str(homeUnderPrice)
                obj = arbObject(sport, league, sportsBook, eventId, period, game, awaySpread,
                                awayPrice, homeSpread, homePrice, awayMoney, homeMoney, drawMoney, total, overPrice,
                                underPrice, awayTotal, awayOverPrice, awayUnderPrice, homeTotal, homeOverPrice, homeUnderPrice)
                dictOfEvents[name] = obj
            else:
                continue
        else:
            continue

x = dictOfEvents.copy()

for key, value in dictOfEvents.items():
    del x[key]
    for keyCopy, valueCopy in x.items():
        if (valueCopy.id == value.id and valueCopy.book != value.book and valueCopy.period == value.period):
            try:
                threeWayCheckArb(value.sport, value.league, valueCopy.book, valueCopy.book, valueCopy.book, value.period, value.game, valueCopy.awayMoney, valueCopy.homeMoney,
                                 valueCopy.drawMoney, '3-Way ML', key, keyCopy, '{}.{}.Draw'.format(value.game[:value.game.index('vs')-1], value.game[value.game.index('vs')+1:]), dataList)
                threeWayCheckArb(value.sport, value.league, value.book, value.book, value.book, value.period, value.game, value.awayMoney, value.homeMoney, value.drawMoney,
                                 '3-Way ML', key, keyCopy, '{}.{}.Draw'.format(value.game[:value.game.index('vs')-1], value.game[value.game.index('vs')+1:]), dataList)
                threeWayCheckArb(value.sport, value.league, value.book, value.book, valueCopy.book, value.period, value.game, value.awayMoney, value.homeMoney,
                                 valueCopy.drawMoney, '3-Way ML', key, keyCopy, '{}.{}.Draw'.format(value.game[:value.game.index('vs')-1], value.game[value.game.index('vs')+1:]), dataList)
                threeWayCheckArb(value.sport, value.league, value.book, valueCopy.book, valueCopy.book, value.period, value.game, value.awayMoney, valueCopy.homeMoney,
                                 valueCopy.drawMoney, '3-Way ML', key, keyCopy, '{}.{}.Draw'.format(value.game[:value.game.index('vs')-1], value.game[value.game.index('vs')+1:]), dataList)
                threeWayCheckArb(value.sport, value.league, valueCopy.book, value.book, value.book, value.period, value.game, valueCopy.awayMoney, value.homeMoney,
                                 value.drawMoney, '3-Way ML', key, keyCopy, '{}.{}.Draw'.format(value.game[:value.game.index('vs')-1], value.game[value.game.index('vs')+1:]), dataList)
                threeWayCheckArb(value.sport, value.league, valueCopy.book, value.book, valueCopy.book, value.period, value.game, valueCopy.awayMoney, value.homeMoney,
                                 valueCopy.drawMoney, '3-Way ML', key, keyCopy, '{}.{}.Draw'.format(value.game[:value.game.index('vs')-1], value.game[value.game.index('vs')+1:]), dataList)
                threeWayCheckArb(value.sport, value.league, valueCopy.book, valueCopy.book, value.book, value.period, value.game, valueCopy.awayMoney, valueCopy.homeMoney,
                                 value.drawMoney, '3-Way ML', key, keyCopy, '{}.{}.Draw'.format(value.game[:value.game.index('vs')-1], value.game[value.game.index('vs')+1:]), dataList)
                twoWayCheckArb(value.sport, value.league, value.book, valueCopy.book, value.period, value.game, value.awayMoney, valueCopy.homeMoney,
                               '2-Way ML', key, keyCopy, '{}.{}'.format(value.game[:value.game.index('vs')-1], value.game[value.game.index('vs')+1:]), dataList)
                twoWayCheckArb(value.sport, value.league, valueCopy.book, value.book, value.period, value.game, valueCopy.awayMoney, value.homeMoney,
                               '2-Way ML', key, keyCopy, '{}.{}'.format(value.game[:value.game.index('vs')-1], value.game[value.game.index('vs')+1:]), dataList)
                if (valueCopy.drawMoney == value.drawMoney == '0.00'):
                    twoWayCheckArb(value.sport, value.league, value.book, value.book, value.period, value.game, value.awayMoney, value.homeMoney,
                                   '2-Way ML', key, keyCopy, '{}.{}'.format(value.game[:value.game.index('vs')-1], value.game[value.game.index('vs')+1:]), dataList)
                    twoWayCheckArb(value.sport, value.league, valueCopy.book, valueCopy.book, value.period, value.game, valueCopy.awayMoney, valueCopy.homeMoney,
                                   '2-Way ML', key, keyCopy, '{}.{}'.format(value.game[:value.game.index('vs')-1], value.game[value.game.index('vs')+1:]), dataList)
                else:
                    continue
                twoWayCheckArb(value.sport, value.league, value.book, value.book, value.period, value.game, value.awayPrice, value.homePrice, 'Spread {}'.format(
                    abs(float(value.awaySpread))), key, keyCopy, '{}.{}'.format(value.game[:value.game.index('vs')-1], value.game[value.game.index('vs')+1:]), dataList)
                twoWayCheckArb(value.sport, value.league, valueCopy.book, valueCopy.book, value.period, value.game, valueCopy.awayPrice, valueCopy.homePrice, 'Spread {}'.format(
                    abs(float(value.awaySpread))), key, keyCopy, '{}.{}'.format(value.game[:value.game.index('vs')-1], value.game[value.game.index('vs')+1:]), dataList)
                twoWayCheckArb(value.sport, value.league, value.book, value.book, value.period, value.game, value.overPrice,
                               value.underPrice, 'Total ({})'.format(abs(float(value.total))), key, keyCopy, 'Over.  Under', dataList)
                twoWayCheckArb(value.sport, value.league, valueCopy.book, valueCopy.book, value.period, value.game, valueCopy.overPrice,
                               valueCopy.underPrice, 'Total ({})'.format(abs(float(value.total))), key, keyCopy, 'Over.  Under', dataList)
                twoWayCheckArb(value.sport, value.league, value.book, value.book, value.period, value.game, value.awayOverPrice,
                               value.awayUnderPrice, 'Away Team Total ({})'.format(abs(float(value.awayTotal))), key, keyCopy, 'Over.  Under', dataList)
                twoWayCheckArb(value.sport, value.league, valueCopy.book, valueCopy.book, value.period, value.game, valueCopy.awayOverPrice,
                               valueCopy.awayUnderPrice, 'Away Team Total ({})'.format(abs(float(value.awayTotal))), key, keyCopy, 'Over.  Under', dataList)
                twoWayCheckArb(value.sport, value.league, value.book, value.book, value.period, value.game, value.homeOverPrice,
                               value.homeUnderPrice, 'Home Team Total ({})'.format(abs(float(value.homeTotal))), key, keyCopy, 'Over.  Under', dataList)
                twoWayCheckArb(value.sport, value.league, valueCopy.book, valueCopy.book, value.period, value.game, valueCopy.homeOverPrice,
                               valueCopy.homeUnderPrice, 'Home Team Total ({})'.format(abs(float(value.homeTotal))), key, keyCopy, 'Over.  Under', dataList)
                if value.awaySpread == valueCopy.awaySpread:
                    twoWayCheckArb(value.sport, value.league, value.book, valueCopy.book, value.period, value.game, value.awayPrice, valueCopy.homePrice, 'Spread {}'.format(
                        abs(float(value.awaySpread))), key, keyCopy, '{}.{}'.format(value.game[:value.game.index('vs')-1], value.game[value.game.index('vs')+1:]), dataList)
                    twoWayCheckArb(value.sport, value.league, valueCopy.book, value.book, value.period, value.game, valueCopy.awayPrice, value.homePrice, 'Spread {}'.format(
                        abs(float(value.awaySpread))), key, keyCopy, '{}.{}'.format(value.game[:value.game.index('vs')-1], value.game[value.game.index('vs')+1:]), dataList)
                if value.total == valueCopy.total:
                    twoWayCheckArb(value.sport, value.league, value.book, valueCopy.book, value.period, value.game, value.overPrice,
                                   valueCopy.underPrice, 'Total ({})'.format(abs(float(value.total))), key, keyCopy, 'Over.  Under', dataList)
                    twoWayCheckArb(value.sport, value.league, valueCopy.book, value.book, value.period, value.game, valueCopy.overPrice,
                                   value.underPrice, 'Total ({})'.format(abs(float(value.total))), key, keyCopy, 'Over.  Under', dataList)
                if value.awayTotal == valueCopy.awayTotal:
                    twoWayCheckArb(value.sport, value.league, value.book, valueCopy.book, value.period, value.game, value.awayOverPrice,
                                   valueCopy.awayUnderPrice, 'Away Team Total ({})'.format(abs(float(value.awayTotal))), key, keyCopy, 'Over.  Under', dataList)
                    twoWayCheckArb(value.sport, value.league, valueCopy.book, value.book, value.period, value.game, valueCopy.awayOverPrice,
                                   value.awayUnderPrice, 'Away Team Total ({})'.format(abs(float(value.awayTotal))), key, keyCopy, 'Over.  Under', dataList)
                if value.homeTotal == valueCopy.homeTotal:
                    twoWayCheckArb(value.sport, value.league, value.book, valueCopy.book, value.period, value.game, value.homeOverPrice,
                                   valueCopy.homeUnderPrice, 'Home Team Total ({})'.format(abs(float(value.homeTotal))), key, keyCopy, 'Over.  Under', dataList)
                    twoWayCheckArb(value.sport, value.league, valueCopy.book, value.book, value.period, value.game, valueCopy.homeOverPrice,
                                   value.homeUnderPrice, 'Home Team Total ({})'.format(abs(float(value.homeTotal))), key, keyCopy, 'Over.  Under', dataList)
            except TypeError:
                continue
        else:
            continue

f.close()
