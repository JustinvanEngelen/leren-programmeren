from data import *


def welkom():
    print("Welkom bij Papi Gelato je mag alle smaken kiezen als het maar vanille smaak is")
def aantalbolletjes():
    doorgaan = True
    while doorgaan == True:
        try:
            aantal = int(input("Hoeveel bolletje(s) wilt u?"))
            aantallen["bolletjes"] += aantal
        except:
            print("Sorry, dat snap ik niet")
            continue

        if aantal > 8:
            print("Sorry, zulke grote bakken hebben we niet")
            continue
            
        elif aantal <= 0:
            print("Sorry, dat snap ik niet")
            
        elif aantal >= 1 and aantal <= 3:
            break

        elif aantal >= 4 and aantal <= 8:
            break

    return aantal

        

def verpakking(aantal:float):
    again = True
    while again == True:
        if aantal >= 4 and aantal <= 8:
            keuze = "bakje"
            aantallen["bakjes"] = aantallen["bakjes"] + 1
            break
        if aantal >= 1 and aantal <= 3:
            keuze=input("Wilt u een bakje of een hoorntje?").lower()
            if keuze == "bakje":
                aantallen["bakjes"] = aantallen["bakjes"] + 1  
                
                break

            elif keuze == "hoorntje":
                aantallen["hoorntjes"] = aantallen["hoorntjes"] + 1
                
                break
            
            else:
                print("Sorry dat snap ik niet")
                continue
    return keuze

def bestelling(keuze:str, aantal:float):
    print("Dan krijgt u een ",aantal," met",keuze,"bolletje(s)")

def meerbestellen():
    meerbestel = True
    while meerbestel == True:
        meerbestellen = input("Wilt u nog meer bestellen? (ja/nee)").lower()
        if meerbestellen == "ja":
            return True
            break
        elif meerbestellen == "nee":
            print("Hier is uw bon")
            return False
            break
        else:
            print("Sorry, dat snap ik niet")
            continue
        
def bonnetje():
    if meerbestellen == "ja":
        bon = False
    bon= True
    totaal = aantallen["bolletjes"]*prijzen["bolletjes"]+aantallen["hoorntjes"]*prijzen["hoorntjes"]+aantallen["bakjes"]*prijzen["bakjes"]
    bolletjesprijs = prijzen["bolletjes"]*aantallen["bolletjes"]
    hoorntjesprijs = prijzen["hoorntjes"]*aantallen["hoorntjes"]
    bakjesprijs = prijzen["bakjes"]*aantallen["bakjes"]
    while bon == True:
        print("----------[Papi Gelato]----------")
        if smakenaantal["a"] >= 1:
            print("B.Aardbei:  ",smakenaantal["a"],"X    1,10    ""€ {:,.2f}".format(smakenaantal["a"]*prijzen["bolletjes"]))
        if smakenaantal["c"] >= 1:
            print("B.Chocolade:",smakenaantal["c"],"X    1,10    ""€ {:,.2f}".format(smakenaantal["c"]*prijzen["bolletjes"]))
        if smakenaantal["m"] >= 1:
            print("B.Munt:     ",smakenaantal["m"],"X    1,10    ""€ {:,.2f}".format(smakenaantal["m"]*prijzen["bolletjes"]))
        if smakenaantal["v"] >= 1:
            print("B.Vanille:  ",smakenaantal["v"],"X    1,10    ""€ {:,.2f}".format(smakenaantal["v"]*prijzen["bolletjes"]))
        if aantallen["hoorntjes"] >= 1:
            print("Hoorntjes:  ",aantallen["hoorntjes"],"X    1,25    ""€ {:,.2f}".format(hoorntjesprijs))
        if aantallen["bakjes"] >= 1:
            print("Bakjes:""     ",aantallen["bakjes"],"X    0,75  ""  € {:,.2f}".format(bakjesprijs))
        print("                       ----------")
        print("Totaal =                    € {:,.2f}".format(totaal))
        print("Bedankt en tot ziens bij Papi Gelato")
        
        break
def kiesjesmaak(aantal:int):
        
    for x in range(1, aantal+1):
        while True:
            smaken = input("Welke smaak wilt u voor bolletje nummer "+str(x)+"? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?")
            if smaken.lower() == "a":
                smakenaantal["a"] += 1
                break
            elif smaken.lower() == "c":
                smakenaantal["c"] += 1
                break
            elif smaken.lower() == "m":
                smakenaantal["m"] += 1
                break
            elif smaken.lower() == "v":
                smakenaantal["v"] += 1
                break
            else:
                print("Sorry, dat snap ik niet. Probeer het opnieuw.")
    return smakenaantal


    


    
