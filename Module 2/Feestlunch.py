from importlib import import_module
import math

acroissant = input  ("hoeveel croissantjes wilt u? ")

croissant = 0.39 * int (acroissant)
astokbrood = input  ("Hoeveel stokbroden wilt u? ")

stokbrood = 2.78 * int (astokbrood)
akorting = input ("Hoeveel kortingsbonnen heeft u? ")

korting = 0.50 * int (akorting)
totaal = int (croissant)+int (stokbrood)-int (korting)


print("De feestlunch kost je bij de bakker ",totaal," euro voor de ",acroissant," croissantjes en de ",astokbrood," stokbroden als de ",akorting," kortingsbonnen nog geldig zijn!")

croissant = int (acroissant) * 0.39
