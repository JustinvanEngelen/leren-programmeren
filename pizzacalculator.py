from importlib import import_module
from logging.config import stopListening
import math
from multiprocessing.resource_sharer import stop

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
    try :
        prijs= int (aantal) * small
    except :
        print ("dat is geen nummer")
        stop
if keuze == "medium":
    try :
        prijs = int (aantal) * medium
    except :
        print ("dat is geen nummer")
        stop
if keuze == "large":
    try :
        prijs = int (aantal) * large
    except :
        print ("dat is geen nummer")
        stop





print ("de prijs is ",prijs,"")

print("------------------------------")
print("|het totale bedrag is ",prijs,"|")
print("------------------------------")