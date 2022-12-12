import random
from fruitmand import fruitmand
lijst=[]
aantal=int(input("hoeveel fruit wilt u? : "))
for fruit in range(len(fruitmand)):
    lijst.append(fruitmand[fruit]["name"])
for p in range(aantal):
    print(random.choice(lijst))


