def naamenleeftijd():
    combis={}
    opniew = True
    leeftijd = 0
    while opniew == True:
        naam = input("Hoe heet u? ")

        if naam != "stop":
            while True:
                leeftijd = (input("Hoe oud bent u? "))
                if leeftijd == "stop":
                    return combis
                try:
                    leeftijd = int(leeftijd)
                    combis[naam] = leeftijd
                    break
                except:
                    if leeftijd != "stop":
                        print("dat is geen getal")
                        continue
                    else:
                        return combis
        else:
            return combis
print(naamenleeftijd())
