from functions import *
from data import *
meer = True

welkom()
klanten=klant()
while meer == True:


    aantal=aantalijs(klanten)
    kiesjesmaak(aantal,klanten)
    if klanten == "2":#zakelijke klant
        break
    
    if klanten == "1":#particuliere klant
        keuze=verpakking(aantal)
        toppings(aantal,keuze)
        bestelling(aantal,keuze)
        meer= meerbestellen()
bonnetje(aantal,klanten)

