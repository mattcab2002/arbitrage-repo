import time
todaysDate = str(time.strftime('%Y-%m-%d'))
f = open("arb.txt", 'r+')
read = f.readlines()


class arbObject:
    def __init__(self, sport, league, book, id, period, game, awaySpread, awayPrice, homeSpread, homePrice, awayMoney, homeMoney, drawMoney,
                 total, overPrice, underPrice, awayTotal, awayOverPrice, awayUnderPrice, homeTotal, homeOverPrice, homeUnderPrice):
        self.sport = sport
        self.league = league
        self.book = book
        self.id = id
        self.period = period
        self.game = game
        self.awaySpread = awaySpread
        self.awayPrice = awayPrice
        self.homeSpread = homeSpread
        self.homePrice = homePrice
        self.awayMoney = awayMoney
        self.homeMoney = homeMoney
        self.drawMoney = drawMoney
        self.total = total
        self.overPrice = overPrice
        self.underPrice = underPrice
        self.awayTotal = awayTotal
        self.awayOverPrice = awayOverPrice
        self.awayUnderPrice = awayUnderPrice
        self.homeTotal = homeTotal
        self.homeOverPrice = homeOverPrice
        self.homeUnderPrice = homeUnderPrice


def negativeAmerican(arb):
    try:
        if float(arb) < 1:
            arb = 1 - (100/int(arb))
        return arb
    except (ValueError, ZeroDivisionError):
        arb = 0
        return arb


def positiveAmerican(arb):
    try:
        if float(arb) > 1:
            arb = 1 + (int(arb)/100)
        return arb
    except ValueError:
        arb = 0
        return arb


def managebet2(stake, odds1, odds2):
    odds1 = float(odds1)
    odds2 = float(odds2)
    sure1 = (1/odds1)
    sure2 = (1/odds2)
    suretotal = sure1 + sure2
    profit = (stake/suretotal) - stake
    profitpercent = (profit/stake)*100
    stake1 = (sure1*stake)/suretotal
    stake2 = (sure2*stake)/suretotal
    return (stake1, stake2, profitpercent)


def managebet3(stake, odds1, odds2, odds3):
    odds1 = float(odds1)
    odds2 = float(odds2)
    odds3 = float(odds3)
    sure1 = (1/odds1)
    sure2 = (1/odds2)
    sure3 = (1/odds3)
    suretotal = sure1 + sure2 + sure3
    profit = (stake/suretotal) - stake
    profitpercent = (profit/stake)*100
    stake1 = (sure1*stake)/suretotal
    stake2 = (sure2*stake)/suretotal
    stake3 = (sure3*stake)/suretotal
    return (stake1, stake2, stake3, profitpercent)


def twoWayCheckArb(sport, league, book1, book2, period, game, arb1, arb2, text, id, idCopy, text2, pass_data):
    count = 0
    realID = '{} && {}'.format(id, idCopy)
    if float(arb1) < 1:
        arb1 = negativeAmerican(arb1)
    else:
        arb1 = positiveAmerican(arb1)
    if float(arb2) < 1:
        arb2 = negativeAmerican(arb2)
    else:
        arb2 = positiveAmerican(arb2)
    try:
        if ((1/arb1) + (1/arb2) < 1) and (managebet2(100, arb1, arb2)[2] >= 1.0) and (managebet2(100, arb1, arb2)[2] <= 15.0):
            for line in read:
                if realID == line[:-1]:
                    count += 1
            if count == 0:
                pass_data.append('\nArbitrage Found \n\nDate: {} \nSport: {} \nLeague: {} \nMarket: {} \nMatchup: {} \nType: {} \n\nBet {:.2f}% of money @ {:.3f} odds on {} on {} \nBet {:.2f}% of money @ {:.3f} odds on {} on {}.\n\nExpect: {:.2f}% ROI \n\nIf lines changed, recalculate here: https://arbitragecalc.com/'.format(
                    todaysDate, sport, league, text, game, period, managebet2(100, arb1, arb2)[0], arb1, text2[:text2.index('.')], book1, managebet2(100, arb1, arb2)[1], arb2, text2[text2.index('.')+3:], book2, managebet2(100, arb1, arb2)[2]))
                f.write(realID+'\n')
                return pass_data
    except ZeroDivisionError:
        return None


def threeWayCheckArb(sport, league, book1, book2, book3, period, game, arb1, arb2, arb3, text, id, idCopy, text2, pass_data):
    count = 0
    realID = '{} && {}'.format(id, idCopy)
    if float(arb1) < 1:
        arb1 = negativeAmerican(arb1)
    else:
        arb1 = positiveAmerican(arb1)
    if float(arb2) < 1:
        arb2 = negativeAmerican(arb2)
    else:
        arb2 = positiveAmerican(arb2)
    if float(arb3) < 1:
        arb3 = negativeAmerican(arb3)
    else:
        arb3 = positiveAmerican(arb3)
    try:
        if (((1/arb1) + (1/arb2) + (1/arb3)) < 1) and (managebet3(100, arb1, arb2, arb3)[3] >= 1.0) and (managebet3(100, arb1, arb2, arb3)[3] <= 15.0):
            for line in read:
                if realID == line[:-1]:
                    count += 1
            if count == 0:
                pass_data.append('\nArbitrage Found \n\nSport: {} \nLeague: {} \nMarket: {} \nMatchup: {} \nType: {} \n\nBet {:.2f}% of money @ {:.3f} odds on {} on {} \nBet {:.2f}% of money @ {:.3f} odds on {} on {} \nBet {:.2f}% of money @ {} odds on {:.3f} on {}. \n\nExpect: {:.2f}% ROI \n\nIf lines changed, recalculate here: https://arbitragecalc.com/'.format(
                    sport, league, text, game, period, managebet3(100, arb1, arb2, arb3)[0], arb1, text2[:text2.index('.')], book1, managebet3(100, arb1, arb2, arb3)[1], arb2, text2[text2.index('.')+2:text2.rindex('.')], book2, managebet3(100, arb1, arb2, arb3)[2], arb3, text2[text2.rindex('.')+1:], book3, managebet3(100, arb1, arb2, arb3)[3]))
                f.write(realID+'\n')
                return pass_data
    except ZeroDivisionError:
        return None
