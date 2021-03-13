buffet = input("Enter your buffet choice: ") 
if buffet == "Korean" :
    Korean = 1500
    today = input("Is today Wednesday (yes/no)? ")
    if today == "no" :
        print("Your payment is %.2f"%Korean,"Baht.")
    elif today == "yes" :
        sum = Korean*85/100
        print("Your payment is %.2f"%sum,"Baht.")      
elif buffet == "Japanese" :
    Japanese = 1000
    today = input("Is today Wednesday (yes/no)? ") 
    if today == "no" :
        print("Your payment is %.2f"%Japanese,"Baht.")
    elif today == "yes" :
        sum = Japanese*85/100
        print ("Your payment is %.2f"%sum,"Baht.")
elif buffet != "Korean" or "Japanese" :
    print("Sorry, there is no",buffet,"buffet.")