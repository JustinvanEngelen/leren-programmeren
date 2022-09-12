from importlib import import_module
import math

#Justin van Engelen
#99074835
#opdracht pizzacalculator

naam = input ("wat is uw naam? :")

small = 6.99
medium = 9.99
large = 12.99

keuze = input ("wilt u een small medium of large pizza :")
aantal = input ("hoeveel pizza's wilt u? :")

if keuze == "small":
    prijs = int (aantal) * small

if keuze == "medium":
    prijs = int (aantal) * medium

if keuze == "large":
    prijs = int (aantal) * large





print ("de prijs is ",prijs,"")

print("------------------------------")
print("|het totale bedrag is ",prijs,"|")
print("------------------------------")