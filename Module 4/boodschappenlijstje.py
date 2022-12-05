boodschappenlijst = {}
repeat = True

while repeat == True:
    product = input("Wat wil je nog aan je boodschappen lijst toevoegen? : ").lower()
    aantal = int(input("Hoeveel wil je daarvan? :  "))

    if product in boodschappenlijst:
            boodschappenlijst[product] = boodschappenlijst[product] + aantal
            repeat = True

    else:
            boodschappenlijst[product] = aantal

    herhaal = input("Wilt u nog meer toevoegen? : ").lower()



    if herhaal == "nee":
        repeat = False


        print("Hier is jou lijst:")
        print("---------------------------")
        for key, value in boodschappenlijst.items():
            print(value,"x ",key)
        print("---------------------------")