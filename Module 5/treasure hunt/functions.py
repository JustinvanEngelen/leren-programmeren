import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HUMAN_COPPER_PER_DAY 
from data import COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_TENT_GOLD_PER_WEEK
from data import COST_HORSE_SILVER_PER_DAY
from data import COST_INN_HUMAN_SILVER_PER_NIGHT
from data import COST_INN_HORSE_COPPER_PER_NIGHT
##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    #deze functie berekent het aantal zilveren munten dat je krijgt voor een aantal koperen munten
    return amount/10

def silver2gold(amount:int) -> float:
    #deze functie berekent het aantal gouden munten dat je krijgt voor een aantal zilveren munten
    return amount/5
def copper2gold(amount:int) -> float:
    #deze functie berekent het aantal gouden munten dat je krijgt voor een aantal koperen munten
    return amount/50

def platinum2gold(amount:int) -> float:
    #deze functie berekent het aantal gouden munten dat je krijgt voor een aantal platina munten
    return amount*25

def getPersonCashInGold(personCash:dict) -> float:
    #deze functie berekent het aantal gouden munten dat een persoon heeft
    return copper2gold(personCash['copper']) + silver2gold(personCash['silver']) + personCash['gold'] + platinum2gold(personCash['platinum'])

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    #deze functie berekent het aantal gouden munten dat je nodig hebt voor voedsel voor een aantal mensen en paarden
    human=copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY*people)*JOURNEY_IN_DAYS
    horse=copper2gold(COST_FOOD_HORSE_COPPER_PER_DAY*horses)*JOURNEY_IN_DAYS
    return round(human+horse,2)

##################### M04.D02.O5 #####################
def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    #deze functie geeft een lijst terug met alle elementen waarvan de key de waarde heeft
    lijst = []
    for x in range(len(list)):
        if list[x][key] == value:
            lijst.append(list[x])
    return lijst


def getAdventuringPeople(people:list) -> list:
    #deze functie geeft een lijst terug met alle mensen die avonturen
    return getFromListByKeyIs(people, "adventuring", True)

def getShareWithFriends(friends:list) -> list:
    #deze functie geeft een lijst terug met alle mensen die hun avonturen delen
    return getFromListByKeyIs(friends, "shareWith", True)

def getAdventuringFriends(friends:list) -> list:
    #deze functie geeft een lijst terug met alle mensen die avonturen en hun avonturen delen
    adventurefriends = []
    adventure = getAdventuringPeople(friends)
    share = getShareWithFriends(friends)

    for x in range(len(adventure)):

        if share[x] in adventure:
            adventurefriends.append(share[x])
    return adventurefriends

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    #deze functie berekent het aantal paarden dat nodig is
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    #deze functie berekent het aantal tenten dat nodig is
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    #deze functie berekent de totale kosten voor het huren van paarden en tenten
    costHorses = JOURNEY_IN_DAYS * horses * silver2gold(COST_HORSE_SILVER_PER_DAY)
    costTents = math.ceil(JOURNEY_IN_DAYS / 7) * tents * COST_TENT_GOLD_PER_WEEK    
    return round(costHorses + costTents, 2)

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    #deze functie geeft een string terug met de items en hun hoeveelheid
    text = ""
    space = ""
    for item in items:
        text += f"{space}{item['amount']}{item['unit']} {item['name']}"
        space = ", "

    return text

def getItemsValueInGold(items:list) -> float:
    #deze functie berekent de totale waarde van de items in goud
    totalPriceInGold = 0

    for item in items:
        priceInGold = item['price']['amount']
        if item['price']['type'] == 'silver':
            priceInGold = silver2gold(priceInGold)
        elif item['price']['type'] == 'copper':
            priceInGold = copper2gold(priceInGold)
        elif item['price']['type'] == 'platinum':
            priceInGold = platinum2gold(priceInGold)

        totalPriceInGold += priceInGold * item['amount']

    return round(totalPriceInGold,2)

#####################M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    #deze functie berekent het totale geldbedrag in goud dat door een lijst van mensen wordt bijgedragen.
    cash = 0
    
    for person in people:
        cash += getPersonCashInGold(person['cash'])

    return round(cash,2)
##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    #deze fuctie geeft een lijst van investeerders terug die een profitReturn hebben van minder dan 10% dus maximaal 9%
    interestingInvestors = []

    for investor in investors:
        if investor["profitReturn"] < 10: #maximaal 9% profitReturn
            interestingInvestors.append(investor)
    
    return interestingInvestors


def getAdventuringInvestors(investors:list) -> list:
    #deze functie geeft een lijst van investeerders terug die een profitReturn hebben van minder dan 10% en die ook avonturiers zijn
    return getFromListByKeyIs(getInterestingInvestors(investors), "adventuring", True)


def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    #deze functie berekent de totale kosten van de investeerders
    adventuringInvestors = getAdventuringInvestors(investors)
    countInvestors = len(adventuringInvestors)
    
    #kosten voor paarden en tenten
    rentalCost = getTotalRentalCost(countInvestors, countInvestors)
    #kosten voor uitrusting
    gearCost = getItemsValueInGold(gear)
    #kosten voor eten
    foodCost = getJourneyFoodCostsInGold(countInvestors, countInvestors)

    return round(rentalCost + gearCost + foodCost,2)

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    #deze functie berekent het maximale aantal nachten dat de groep kan overnachten
    people_per_night_gold = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horses_per_night_gold = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    return int(leftoverGold / (people_per_night_gold + horses_per_night_gold))


def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    #deze functie berekent de kosten voor overnachtingen in de herberg
    gold_per_night = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT)
    horses_gold_per_night = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT)
    human_per_night_Gold =  gold_per_night * people 
    horses_per_night_Gold = horses_gold_per_night * horses 
    return round((human_per_night_Gold + horses_per_night_Gold) * nightsInInn,2)


##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    #deze functie berekent de winst per investeerder
    investorlist = []
    for x in investors:
        if x['profitReturn'] < 10: #maximaal 9% profitReturn
            investorlist.append(round(x['profitReturn'] / 100 * profitGold,2) )
    return investorlist
    

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    #deze functie berekent de winst per persoon voor een groep avonturiers na aftrek van de investeerderskosten.
    investor_cuts = 0
    for a in investorsCuts:
        investor_cuts += a
    return round((profitGold - investor_cuts) / fellowship,2)

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()