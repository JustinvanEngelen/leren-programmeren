import random
opnieuw = True
boodschappenlijst={

}
while opnieuw == True:
    wat = input ("wat wil u aan het lijstje toevoegen : ").lower()
    try:
        hoeveel = int(input ("hoeveel wilt u daarvan toevogen : "))
        boodschappenlijst.update({hoeveel:wat})
    except: 
        print("dat is geen getal")
    meer = input ("wilt u nog iets : ").lower()
    if meer == "ja":
        continue
    if meer == "nee":
        opnieuw==False
        break
    else:
        break
print("-[Boodschappenlijstje]-")
print(boodschappenlijst)
print("________________________")

    


 