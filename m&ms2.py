import random
zak=["rood", "blauw", "groen", "geel" , "bruin"]
vraag = int(input ("Hoeveel m&ms wilt u toevoegen? : "))
thisdict = {
    "rood":0,
    "groen":0,
    "geel":0,
    "bruin":0,
    "blauw":0
}
for x in range (vraag):
    sigma=random.choice(zak)
    thisdict[sigma]=thisdict[sigma] +1
print(thisdict)