import math
loop =True
def tafels(getal:int):

    for x in range (11):
        antwoord = x*getal
        print(x, "x" ,getal, "=", antwoord )
while loop == True:
    try:
        getal = int(input("welk getal wilt u de tafel van : "))
        loop = False
    except:
        print("dat is geen getal")
        continue

tafels(getal)