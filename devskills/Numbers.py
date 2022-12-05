list1=[]
delen = 0
for x in range(19):
    try:
        nummer = int(input ("welk getal kiets u : "))
        list1.append(nummer)
    except:
        continue
    list1.sort()
result = list(filter(lambda x: (x % 3 == 0), list1))
print("kleintste getal is ", list1[0])
print("grootste getal is ", list1[-1])
print(len(result))