from functions import *
from data import *
meer = True
while meer == True:
    welkom()
    aantal=aantalbolletjes()
    keuze=verpakking(aantal)
    bestelling(aantal,keuze)
    meer= meerbestellen()
bonnetje(aantal,keuze,hoorntjesaantal=0,bakjesaantal=0)