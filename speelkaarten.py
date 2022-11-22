import random
deck=[" joker"," joker"]
stapel=[]
kleuren = [" harten", " klaveren", " schoppen", " ruiten"]
kaarten = [" 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9"," 10"," boer", "  vrouw", "  heer", "  aas"]
for j in range(4):
    for x in range(13):
        sigma=kleuren[j]+kaarten[x]
        deck.append(sigma)
random.shuffle(deck)
for p in range(1,8):
    print("Kaart ",p,"",deck.pop(0))
print(" deck(47 kaarten)",deck)
