leeftijd = input ("wat is uw leeftijd")
leeftijd=int(leeftijd)
if leeftijd >= 18:
    print ("U mag naar binnen")
    naam = input ("wat is uw naam?")
    if leeftijd <= 21:
        if naam == "Rudi" or "arnold" or "jeroen" or "kjeld" :
            print ("u krijgt een sticker")
        else:
            print("U mag naar binnen maar u krijgt geen bandje")