def showwelcome(welcometo:str,aantal:int):
    for i in range(aantal):
        print("Hello from function "+welcometo+str(i+1)+"!")
where ='town '
aantal = int(input("Hoe veel keer wilt je dit printen"))
showwelcome(where,aantal)
