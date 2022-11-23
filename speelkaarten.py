import random
deck=[" joker"," joker"]
kleuren = ["harten", "klaveren", "schoppen", "ruiten"]
kaarten = ["2","3","4","5","6","7","8","9","10","boer", "vrouw", "heer", "aas"]
for j in range (len(kleuren)):
    for x in range(len(kaarten)):
        sigma=kleuren[j]+ " "+kaarten[x]
        deck.append(sigma)
random.shuffle(deck)
for p in range(1,8):
    print("Kaart ",p,"",deck.pop(0))
print(deck)
print("",len(deck), "kaarten")
