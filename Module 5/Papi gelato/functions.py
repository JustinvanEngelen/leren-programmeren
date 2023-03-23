from data import *

def welkom():
    print("Welkom bij Papi Gelato je mag alle smaken kiezen als het maar vanille smaak is")
def aantalbolletjes():
    boninformatie=[]
    doorgaan = True
    while doorgaan == True:
        try:
            aantal = int(input("Hoeveel bolletje(s) wilt u?"))
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
    bakjesaantal = 0
    hoorntjeaantal = 0
    again = True
    while again == True:
        if aantal >= 4 and aantal <= 8:
            keuze = "bakje"
            bakjesaantal+=1
            break
        if aantal >= 1 and aantal <= 3:
            keuze=input("Wilt u een bakje of een hoorntje?").lower()
            if keuze == "bakje":
                bakjesaantal=bakjesaantal+1  
                
                break

            elif keuze == "hoorntje":
                hoorntjeaantal= hoorntjeaantal+1
                
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
            print("Bedankt en tot ziens!")
            return False
            break
        else:
            print("Sorry, dat snap ik niet")
            continue
        
def bonnetje(aantal:float, keuze:str, hoorntjesaantal:float, bakjesaantal:float):
    if meerbestellen == "ja":
        bon = False
    bon= True
    while bon == True:
        print("----------[Papi Gelato]----------")
        if aantal > 0:
            print("Bolletjes:",aantal,"Bolletjes €",bolletjes*aantal)
        break