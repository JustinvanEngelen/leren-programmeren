from fruitmand import fruitmand
kleuren = []
fruitmand.remove({'name' : 'druif', 'weight' : 5, 'color' : 'purple', 'round' : True})
for i in range (len(fruitmand)):
    kleur = (fruitmand[i]['color'])
    if kleur not in kleuren:
        kleuren.append(kleur)
print (kleuren)