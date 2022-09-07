from importlib import import_module
import math


acroissant = 17
croissant = 0.39 * acroissant

astokbrood = 2
stokbrood = 2.78 * astokbrood

akorting= 3
korting = 0.50 * akorting
totaal = 10.69
print(croissant+stokbrood-korting)

print("De feestlunch kost je bij de bakker ",totaal," euro voor de ",acroissant," croissantjes en de ",astokbrood," stokbroden als de ",akorting," kortingsbonnen nog geldig zijn!")
