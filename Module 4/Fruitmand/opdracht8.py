from fruitmand import fruitmand
totaal = 0 
fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 3500,
    'color' : 'red',
    'round' : True})
for fruit in range(len(fruitmand)):
        gewicht = fruitmand[fruit]['weight']
        totaal = totaal + gewicht
print(totaal)
