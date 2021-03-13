Price = float(input("Total Price: "))
if Price < 50 :
    print("You got: 0")
elif Price > 50 :
    sum = Price//50
    print("You got:",int(sum))