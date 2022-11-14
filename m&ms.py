import random

lijst =[]
thistuple=["oranje", "blauw", "groen", "bruin"]
aantal = input ("hoeveel M&Ms moet er toegevoegd worden")
aantal=int(aantal)
for x in range (aantal):
    lijst.append(random.choices(thistuple))
print(lijst)