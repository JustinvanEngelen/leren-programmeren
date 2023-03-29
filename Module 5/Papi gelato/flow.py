from functions import *
from data import *
meer = True



welkom()
while meer == True:
    aantal=aantalbolletjes()







    kiesjesmaak(aantal)
    keuze=verpakking(aantal)
    bestelling(aantal,keuze)
    meer= meerbestellen()
bonnetje()

