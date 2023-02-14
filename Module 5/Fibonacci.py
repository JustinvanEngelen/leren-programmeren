cijfers = [0]
def fibonaccireeks(aantal:int):
    oudgetal = 0 
    nieuwgetal = 1 
    som = oudgetal + nieuwgetal
    cijfers.append(som) 
    for i in range(aantal): 
        volgende = cijfers.append(cijfers[oudgetal]+cijfers[nieuwgetal])
        oudgetal += 1
        nieuwgetal += 1
    print(cijfers) 
    return cijfers
fibonaccireeks(20)

