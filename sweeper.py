from random import randint


play = True
bom = randint(1,2)
ronde=1
ronde = int (ronde)
    
    
while play == True:
    gok = input ("U bent in ronde "+str(ronde)+"op wek getal van 1 tot 10 denkt u dat dat de bom is ?")
    gok=int (gok)
    if bom == gok:
        print ("BOEM, game over")
        quit()
    else:
        print ("wilt u naar ronde ",ronde,"?")
        vraag = input ("Ja of Nee").lower()
        if vraag == "ja":
            ronde = ronde+1
            play = True
        else:
            print("U bent geeindigd op ronde ",ronde-1,"")
            play = False
    pass