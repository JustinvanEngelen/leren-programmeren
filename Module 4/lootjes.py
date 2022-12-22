import random
loop=True
opnieuw = True
lijst=[]
while loop == True:
    naam = input("Geef uniek naam/namen : ").lower()
    if naam in lijst:
        print("die naam zit er al in")
        continue
    else:
        lijst.append(naam)     
        if len(lijst) >=3:
            loop=False
while opnieuw == True:
    meer = input("Wil je meer namen toevoegen? : ").lower()
    if meer =="ja":
        wie=input("wie wil je nog meer toevoegen? : ").lower()
        if wie in lijst:  
            print("die naam zit er al in")
            continue
        else:
            lijst.append(wie)
    else:
        opnieuw=False
        random.shuffle(lijst)

        for x in range (len(lijst)):
            if len(lijst)<= x+1:
                print(lijst[x],"heeft",lijst[0])
            else:
                print(lijst[x],"heeft",lijst[x+1])