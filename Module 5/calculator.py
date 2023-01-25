opnieuw = True
def calculator():
    while opnieuw == True:
        print("wat wilt u doen?")
        print("A) Gettallen optellen?")
        print("B) Getallen aftrekken?")
        print("C) Getallen vermenigvuldigen?")
        print("D) Getallen delen?")
        print("E) Getal ophogen?")
        print("F) Getal verlagen")
        print("G)Getal verdubbelen")
        print("H)Getal halveren?")
        print("I) niets?")
        choice=input("Kies(A,B,C,D,E,F,G,H) : ").capitalize()
        if choice =="A":
            print("Goeie keuze")
        
calculator()
