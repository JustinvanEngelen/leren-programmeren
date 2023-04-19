from functions import *
from data import *
meer = True

welkom()
klanten=klant()
while meer == True:


    aantal=aantalbolletjes(klanten)
    kiesjesmaak(aantal,klanten)
    if klanten == "2":
        break
    if klanten == "1":
        keuze=verpakking(aantal)
        toppings()
        bestelling(aantal,keuze)
        meer= meerbestellen()
bonnetje(aantal)

