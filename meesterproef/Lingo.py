from lingowords import *
import random

def random_word():
    list = []
    woord = random.choice(words)
    list.append(woord)
    return woord
def eerst_letter():
    randomwoord = random_word()
    eersteletter = randomwoord[0]
    print("Het woord begint met een " + eersteletter)
    return randomwoord
def woord_raden(list : list):
    for x in range(5):
        woordraden = input("Raad het woord: ")
        if woordraden == random_word():
            print("Gefeliciteerd, je hebt het woord geraden!")
            break
        else:
            print("Helaas, je hebt het woord niet geraden.")
            print("Het woord was " + str(list))
            break