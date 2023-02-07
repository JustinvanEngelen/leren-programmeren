def calculator():
    opnieuw = False
    delen=True
    vraag=True
    getal1=0
    aantal=0
    while vraag == True:
        try:
            totaal= float(input("welk getal wilt u gebruiken?"))
            vraag=False
        except:
            print("dat is geen nummer")
    while opnieuw == False:
        print("wat wilt u doen?")
        print("A) Gettallen optellen?")
        print("B) Getallen aftrekken?")
        print("C) Getallen delen?")
        print("D) Getallen vermenigvuldigen?")
        print("E) Getal ophogen?")
        print("F) Getal verlagen")
        print("G)Getal verdubbelen")
        print("H)Getal halveren?")
        print("I) niets?")
        choice=input("Kies(A,B,C,D,E,F,G,H) : ").capitalize()
        if choice =="A":
            vraag=True
            print("Gettallen optellen")
            while vraag ==True:
                try:
                    getal2= float(input("kies welk getal waarmee u wilt optellen : "))
                except:
                    print("Dat is geen getal")
                    continue
                vraag =False
                getal1 =(getal1-getal1)+totaal
                totaal=totaal+getal2
                print(getal1,"+",getal2 ,"=",totaal)
                aantal=aantal+1
                continue
        if choice =="B":
            vraag=True
            print("Gettallen aftrekken")
            while vraag == True:
                try:
                    getal2= float(input("kies welk getal waarmee u wilt aftrekken : "))
                except:
                    print("dat is geen getal")
                    continue
                vraag = False
                getal1 =(getal1-getal1)+totaal
                totaal=totaal-getal2
                print(getal1,"-",getal2 ,"=",totaal)
                aantal=aantal+1
                continue
        if choice =="C":
            delen=True
            print("Gettallen delen")
            while delen== True:
                try:
                    getal2= float(input("kies welk getal waarmee u wilt delen : "))
                except:
                    print("Dat is geen getal")
                    continue
                if getal2 == float("0"):
                    print("u kan nietdoor 0 delen")
                    continue
                else:
                    delen=False
                    getal1 =(getal1-getal1)+totaal
                    totaal=totaal/getal2
                    print(getal1,":",getal2 ,"=",totaal)
                    aantal=aantal+1
                    continue
        if choice =="D":
            vraag = True
            print("Gettallen vermenigvuldigen")
            while vraag == True:
                try:
                    getal2= float(input("kies welk getal waarmee u wilt vermenigvuldigen : "))
                except:
                    print("dat is geen getal")
                    continue
                vraag=False
                getal1 =(getal1-getal1)+totaal
                totaal=totaal*getal2
                print(getal1,"X",getal2 ,"=",totaal)
                aantal=aantal+1
                continue
        if choice =="E":
            print("Gettallen ophogen")
            getal1 =(getal1-getal1)+totaal
            totaal=totaal+1
            print(getal1,"+ 1 =",totaal)
            aantal=aantal+1
            continue
        if choice =="F":
            print("Gettallen verlagen")
            getal1 =(getal1-getal1)+totaal
            totaal=totaal-1
            print(getal1,"- 1 =",totaal)
            aantal=aantal+1
            continue
        if choice =="G":
            print("Gettallen verlagen")
            getal1 =(getal1-getal1)+totaal
            totaal=totaal*2
            print(getal1,"X 2 =",totaal)
            aantal=aantal+1
            continue
        if choice =="H":
            print("Gettallen verlagen")
            getal1 =(getal1-getal1)+totaal
            totaal=totaal/2
            print(getal1,": 2 =",totaal)
            aantal=aantal+1
            continue
        if choice =="H":
            print("A) Gettallen verlagen")
            getal1 =(getal1-getal1)+totaal
            totaal=totaal/2
            print(getal1,": 2 =",totaal)
            aantal=aantal+1
            continue
        if choice =="I":
            if aantal<=0:
                print("u moet nog een berekening doen")
                continue
            if aantal>=0:
                opnieuw=True
                print("uw laatste antwoord was",totaal)
calculator()

