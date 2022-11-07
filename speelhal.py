from importlib import import_module
import math

ppl = input("met hoevel personen bent u? ")
ticket = 7.45 * int(ppl)
a = 5
tijd = input ("hoelang wilt u? ")
prijs = int (tijd)/(a)
vrbril= 0.37 * (prijs)
totaal = int (ticket)+int (vrbril)


print("Dit geweldige dagje-uit met ",ppl," mensen in de Speelhal met ",tijd," minuten VR kost je maar ",totaal," euro")
