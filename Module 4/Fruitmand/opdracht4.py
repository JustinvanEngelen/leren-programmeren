import random
from fruitmand import fruitmand
lijst=[]
vraag = True
while vraag == True:
    try:
        aantal=int(input("hoeveel fruit wilt u? : "))
    except:
        continue
    vraag = False
    for fruit in range(len(fruitmand)):
        lijst.append(fruitmand[fruit]["name"])
    for p in range(aantal):
        print(random.choice(lijst))