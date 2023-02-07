def reeks(n):
   if n <= 1:
       return n
   else:
       return(reeks(n-1) + reeks(n-2))
try:
    aantal = int(input("Hoeveel getallen? :  "))
except:
    print("Dat is geen getal!")
    quit()
if aantal <= 0:
   print("Doe iets boven 0!")
else:
   print("Fibonacci reeks:")
   for x in range(aantal):
    print(reeks(x))