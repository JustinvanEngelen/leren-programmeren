from time import sleep
from tkinter import W

begin = input ("Doet u mee aan de heist?y/n ").lower()
if begin == "y":
    print("Dankuwel dat u meedoet aan deze missie")
else:
    if begin =="n":
        print ("Neem geen contact op")
sleep(2)
print("Uw codenaam is Meneer Frog")
sleep(2)
print("Jullie gaan naar de jewelry met een onopvallende auto")
sleep(2)
print("je bent aangekomen en gaan allebei via de ladder rop het dak")
sleep(2)
print("Er is een extra dak boven waar het makkelijker is om binnen te komen")
sleep(2)
vraag1 = input("wil je met de jetpack of met de enderpearl?").lower()
if vraag1 == "jetpack":
    vraag2= input ("Wil je een harde landing of zachte landing").lower()
    if vraag2 == "harde landing":
        print ("Je land te hard op het dak je valt door het dak en je word neer geschoten")
    else:
        if vraag2 == "zachte landing" :
            print("Goede keuze je bent veilig op het dak")
else :
    if vraag1 == "enderpearl":
        print ("You died je gooide de enderpearl in het riool")
        quit()
sleep(2)
print("je ziet een open raam je klimt  naar binnen")
sleep(2)
print ("er komt een bewaker aan welk voorwerp gebruik")
sleep(2)
vraag3 = input ("wil je de pokebal of de speed potion of de boomerang of de vlugge ugge").lower()
if vraag3 == "pokeball" :
    print ("Je klikt op het knopje op de pokebal en je vangt je zelf")
    quit()
else:
    if vraag3 == "speed potion" :
        print("De speed potion geeft geen versnelde reactie tijd dus knal je tegen een muur")
    else:
        if vraag3 == "boomerang":
            print("Je gooit de boomerang maar hij komt terug tegen je hoofd")
        else:
            if vraag3 == "vlugge ugge":
                print("Goede keuze je rijd weg met de vlugge ugge")
sleep(2)
print("Je ziet de diamand")
print("maar het alarm gaat af hoe ga je escapen")
vraag4 = input ("ga je met de bom of met de granaat of doe je niks en denk je even goed na").lower()
if vraag4 == "bom" :
    print ("Je zet de bom aan en hij blies gelijk op toen je er naast stond")
else:
    if vraag4 == "granaat" :
        print("Je gooide de granaat tegen de muur en hij kaatste terug naar jou en ontplofte")
    else:
        if vraag4 == "niks" :
            print("Je deed niks dus ging je maar door de voordeur")
            sleep(2)
            print("de politie is er bijna dus neem je snel de onopvallende auto terug naar de thuisbasis")
            sleep(2)
            print("Je bent escaped je bent veilig terug met de grote zeldzame diamant")


