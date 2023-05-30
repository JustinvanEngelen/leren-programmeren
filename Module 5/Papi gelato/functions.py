from data import *

#--------------------------Welkom---------------------------------------------------------------------------------------------#
def welkom():
    print("Welkom bij Papi Gelato")
#--------------------------klant---------------------------------------------------------------------------------------------#
def klant():
    while True:
        klanten = input("Bent u 1) een particuliere klant of 2) een zakelijke klant?")
        if klanten == "1" or klanten == "2":
            return klanten
        else:
            print("Sorry dat is geen optie die we aanbieden")
            continue
#--------------------------Aantal bolletjes---------------------------------------------------------------------------------------------#

def aantalbolletjes(klanten:str):
    doorgaan = True
    while doorgaan == True:
        if klanten == "2":
            try:
                liter = int(input("Hoeveel liter ijs wilt u?"))
                aantallen["liter"] += liter
                if liter <=0:
                    print("Sorry dat is geen optie die we aanbieden")
                    continue
               
                return liter
               
            except:
                print("Sorry dat is geen optie die we aanbieden")
                continue
        if klanten == "1":
            try:
                aantal = int(input("Hoeveel bolletje(s) wilt u?"))
                aantallen["bolletjes"] = aantallen["bolletjes"] + aantal
                
            except:
                print("Sorry dat is geen optie die we aanbieden")
                continue
        

            if aantal > 8:
                print("Sorry, zulke grote bakken hebben we niet")
                continue
                
            elif aantal <= 0:
                print("Sorry dat is geen optie die we aanbieden")
                
            elif aantal >= 1 and aantal <= 3:
                break

            elif aantal >= 4 and aantal <= 8:
                break
    

    return aantal

        
#--------------------------Verpakking---------------------------------------------------------------------------------------------#
def verpakking(aantal:int):
    again = True
    while again == True:
        if aantal >= 4 and aantal <= 8:
            keuze = "bakje"
            aantallen["bakjes"] = aantallen["bakjes"] + 1
            prijzen["caramel"] = prijzen["caramel"] =0.90
            break
        if aantal >= 1 and aantal <= 3:
            keuze=input("Wilt u een bakje of een hoorntje?").lower()
            if keuze == "bakje":
                prijzen["caramel"] = prijzen["caramel"] = 0.90
                aantallen["bakjes"] = aantallen["bakjes"] + 1
                break
            if keuze == "hoorntje":
                aantallen["hoorntjes"] = aantallen["hoorntjes"] + 1
                prijzen["caramel"] = prijzen["caramel"] = 0.60

                break

        
            
            else:
                print("Sorry dat is geen optie die we aanbieden")
                continue
    return keuze
#--------------------------Bestelling---------------------------------------------------------------------------------------------#
def bestelling(keuze:str, aantal:int):
    print("Dan krijgt u een ",aantal," met",keuze,"bolletje(s)")
#--------------------------Meer bestellen---------------------------------------------------------------------------------------------#
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
            print("Sorry dat is geen optie die we aanbieden")
            continue
#--------------------------Bonnetje---------------------------------------------------------------------------------------------#
def bonnetje(aantal:int , klanten:str):
    bon= True
    
    
    hoorntjesprijs = aantallen["hoorntjes"] * prijzen["hoorntjes"]
    bakjesprijs = aantallen["bakjes"] * prijzen["bakjes"]
    slagroomprijs= toppingsaantal["slagroom"] * prijzen["slagroom"]
    bcaramelprijs = toppingsaantal["caramelbakje"] * prijzen["caramelbakje"]
    hcaramelprijs = toppingsaantal["caramelhoorntje"] * prijzen["caramelhoorntje"]
    sprinkelsprijs = toppingsaantal["sprinkels"] * prijzen["sprinkels"]

    if klanten =="1":
        totaalprijs = aantallen["bolletjes"] * prijzen["bolletjes"] + aantallen["hoorntjes"] * prijzen["hoorntjes"] + aantallen["bakjes"] * prijzen["bakjes"] + toppingsaantal["slagroom"] * prijzen["slagroom"] + toppingsaantal["caramelbakje"] * prijzen["caramelbakje"] + toppingsaantal["caramelhoorntje"] * prijzen["caramelhoorntje"] + toppingsaantal["sprinkels"] * prijzen["sprinkels"]
    if klanten =="2":
        totaalprijs = aantallen["liter"] * prijzen["liter"]
        


    

    
    while bon == True:
        print("-----------[Papi Gelato]-----------")
        if litersmakenaantal["a"] >= 1:
            print("L.Aardbei:  ",litersmakenaantal["a"],"X    € 9,80   ""€ {:,.2f}".format(litersmakenaantal["a"]*prijzen["liter"]))
        if litersmakenaantal["c"] >= 1:
            print("L.Chocolade:",litersmakenaantal["c"],"X    € 9,80   ""€ {:,.2f}".format(litersmakenaantal["c"]*prijzen["liter"]))
        if litersmakenaantal["v"] >= 1:
            print("L.Vanille:  ",litersmakenaantal["v"],"X    € 9,80   ""€ {:,.2f}".format(litersmakenaantal["v"]*prijzen["liter"]))


        if smakenaantal["a"] >= 1:
            print("B.Aardbei:  ",smakenaantal["a"],"X    € 0,95   ""€ {:,.2f}".format(smakenaantal["a"]*prijzen["bolletjes"]))
        if smakenaantal["c"] >= 1:
            print("B.Chocolade:",smakenaantal["c"],"X    € 0,95   ""€ {:,.2f}".format(smakenaantal["c"]*prijzen["bolletjes"]))
        if smakenaantal["v"] >= 1:
            print("B.Vanille:  ",smakenaantal["v"],"X    € 0,95   ""€ {:,.2f}".format(smakenaantal["v"]*prijzen["bolletjes"]))


        if aantallen["hoorntjes"] >= 1:
            print("Hoorntjes:  ",aantallen["hoorntjes"],"X    € 1,25   ""€ {:,.2f}".format(hoorntjesprijs))
        if aantallen["bakjes"] >= 1:
            print("Bakjes:""     ",aantallen["bakjes"],"X    € 0,75 ""  € {:,.2f}".format(bakjesprijs))


        if toppingsaantal["slagroom"] >= 1:
            print("Slagroom:   ",toppingsaantal["slagroom"],"X    €","{:,.2f}".format(prijzen["slagroom"]),"  ""€ {:,.2f}".format(slagroomprijs))
        if toppingsaantal["sprinkels"] >= 1:
            print("Sprinkels:  ",toppingsaantal["sprinkels"],"X    €","{:,.2f}".format(prijzen["sprinkels"]),"  ""€ {:,.2f}".format(sprinkelsprijs))
        if toppingsaantal["caramelbakje"] >= 1:
            print("B.Caramel:  ",toppingsaantal["caramelbakje"],"X    €","{:,.2f}".format(prijzen["caramelbakje"]),"  ""€ {:,.2f}".format(bcaramelprijs))
        if toppingsaantal["caramelhoorntje"] >= 1:
            print("H.Caramel:  ",toppingsaantal["caramelhoorntje"],"X    €","{:,.2f}".format(prijzen["caramelhoorntje"]),"  ""€ {:,.2f}".format(hcaramelprijs))

        

        print("                        -----------")
        print("Totaal =                     € {:,.2f}".format(totaalprijs))
        


        if klanten == "2":
            print("BTW (6%) =                   € {:,.2f}".format(totaalprijs/106*6))
        print("Bedankt en tot ziens bij Papi Gelato")

        
        break
#--------------------------smaken---------------------------------------------------------------------------------------------#
def kiesjesmaak(aantal:int , klanten:str):
        
    for x in range(1, aantal+1):
        while True:
            if klanten == "1":
                smaken = input("Welke smaak wilt u voor bolletje nummer "+str(x)+"? A) Aardbei, C) Chocolade of V) Vanille?").lower()
                if smaken == "a":
                    smakenaantal["a"] += 1
                    break
                elif smaken == "c":
                    smakenaantal["c"] += 1
                    break

                elif smaken == "v":
                    smakenaantal["v"] += 1
                    break
                else:
                    print("Sorry dat is geen optie die we aanbieden.")
                    continue
            elif klanten == "2":
                smaken=input("Welke smaak wilt u voor liter nummer "+str(x)+"? A) Aardbei, C) Chocolade of V) Vanille?").lower()
                if smaken == "a":
                    litersmakenaantal["a"] += 1
                    break
                elif smaken == "c":
                    litersmakenaantal["c"] += 1
                    break

                elif smaken == "v":
                    litersmakenaantal["v"] += 1
                    break
                else:
                    print("Sorry dat is geen optie die we aanbieden.")
                    continue
    return smakenaantal
#--------------------------toppings---------------------------------------------------------------------------------------------#
def toppings(aantal:int, keuze:str):
    while True:
        toppingvraag=input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?").lower()
        if aantal >= 4 and aantal <= 8:
            if toppingvraag == "d":
                toppingsaantal["caramelbakje"] += 1
                break
        if aantal >= 1 and aantal <= 3:
            if keuze == "hoorntje":
                if toppingvraag == "d":
                    toppingsaantal["caramelhoorntje"] += 1
                    break
            if keuze == "bakje":
                if toppingvraag == "d":
                    toppingsaantal["caramelbakje"] += 1
                    break
        if toppingvraag == "a":
            break
        elif toppingvraag == "b":
            toppingsaantal["slagroom"] += 1
            break
        elif toppingvraag == "c":
            toppingsaantal["sprinkels"] += 1 * aantal
            break
        else:
            print("Sorry dat is geen optie die we aanbieden.")
            continue



