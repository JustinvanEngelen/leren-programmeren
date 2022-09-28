am = True
pm = True
tijd = 0
tijd = int(tijd)

while am == True:
    print ("",tijd,"AM")
    tijd = tijd + 1
    if tijd <= 12:
        am = True
    else:
        am=False
while pm == True:
    print("",tijd,"PM")
    tijd = tijd + 1
    if tijd < 24:
        pm = True
    else:
        pm = False