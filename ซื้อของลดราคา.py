TV = int(input("How many TVs? ")) 
DVD = int(input("How many DVD players? ")) 
Audio = int(input("How many Audio Systems? ")) 
Price = 6000*TV + 1500*DVD + 3000*Audio
if TV >= 0 and DVD >= 0 and Audio >= 0 and Price < 24000 :
    print("Total price is %.2f"%Price,"baht.")
    print("Your payment is %.2f"%Price,"baht. Thank you!")
elif TV >= 0 and DVD >= 0 and Audio >= 0 and Price >= 24000 :
    discount = Price*20/100
    sum = Price*80/100
    print("Total price is %.2f"%Price,"baht.")
    print("You've got a discount of %.2f"%discount,"baht.")
    print("Your payment is %.2f"%sum,"baht. Thank you!")