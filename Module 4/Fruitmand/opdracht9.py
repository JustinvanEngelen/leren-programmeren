from fruitmand import fruitmand
kleuren = []
fruitmand.pop(4)
for i in range (len(fruitmand)):
    kleur = (fruitmand[i]['color'])
    if kleur not in kleuren:
        kleuren.append(kleur)
print (kleuren) 