import random
ronde=1
gok = 0
gokken=0
while ronde<=20:
    randoom= random.randint(1,1000)
    while gokken <=10:
        gokken = gokken + 1
        gok=input("welk getal gokt u tussen 1 en 1000: ")
        gok = int(gok)
        if gok == randoom:
            print("geraden")
            gokken=gokken+1
            volgende=input("Nog een getal raden? ja/nee: ").lower()
            if volgende=="ja":
                    ronde=ronde+1
                    break
            else:
                volgende=="nee"
                print(ronde)
                quit()
        elif gok >= randoom:
            print("lager")
            warm = gok-randoom
            if warm >=25:
                print("je bent warm")
            if warm <=25:
                print("je bent warm")
        elif gok <= randoom:
            print("hoger")
            warm = gok-randoom
            if warm >=50:
                print("je bent warm")
            if warm <=50:
                print("je bent warm")
    print("je hebt al 10 ronde gedaan je score is ",ronde,"")