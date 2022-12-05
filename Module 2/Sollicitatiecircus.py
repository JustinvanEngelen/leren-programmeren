print("-----------------------------------------------------")
print("Sollicitatie Circusdirecteur voor Circus HotelDeBotel")
print("hier komen de vragen")
print("-----------------------------------------------------")
naam = input ("wat is uw naam?")
if naam == ("deviyano") :
    raise NameError ("You shall not pass")
if naam == ("tim") :
    raise NameError ("you are not allowed")
if naam == ("spongebob") :
    raise NameError ("Go back to bikini bottom")
ervaring = input ("heeft u ervaring met dieren-jongleren of acrobatiek")
jaar = input ("Hoeveel jaar ervaring heeft u?")
diploma = input ("welke diploma heeft u?")
rijbewijs = input ("welk rijbewijs heeft u?") 
hoed = input ("bent u in bezit van een hoge hoed")
geslacht = input ("bent u een man of een vrouw?")

if geslacht == "man" :
    haar = input ("hoelang is uw haar")
if geslacht == "vrouw" :
    haar = input ("hoelang is uw haar")      

lengte = input ("hoelang bent u?")
gewicht = input ("how zwaar bent u?")
certificaat = input ("heeft u het certificaat overleven met gevaarlijk personeel")
randomvraag1 = input ("heeft u een clownsneus?")
randomvraag2 = input ("heb je een broer of zus?")
randomvraag3 = input ("wat was je vorige baan?")
randomvraag4 = input ("heeft u huisdieren?")

goed = False
if ervaring == "dieren" or "jongleren" or "acrobatiek" :
    if jaar == "5" or "4" or "3" :
        if   rijbewijs == "vrachtwagen" :
            if hoed == "ja" :
                if haar >= "10" or "20" :
                    if lengte >= "150" :
                        if gewicht >= "90" :
                            goed = True
                            if goed == True :
                             print ("",naam,"Gefeliciteerd u bent perfect voor deze baan, u krijgt binnekort een mail.")

if goed == False:
    print ("",naam,"Sorry jenkomt niet in aanraking met deze baan")