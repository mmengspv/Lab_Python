print("---<< Main Menu >>---")
print("%17s"%"<B>urger Meal")
print("%18s"%"<C>hicken Meal")
print("%16s"%"<P>asta Meal")
main = input("Enter your choice: ")
if main == "B" or main == "b" :
    print("---<< Burger Sub Menu >>---")
    print("%20s"%"<R>egular Burger")
    print("%19s"%"<C>heese Burger")
    print("%26s"%"<D>ouble Cheese Burger")   
    sub = input("Enter your choice: ")
    if sub == "R" or sub == "r" :
        sub_menu = "Regular Burger"
        sum = 60
        print("Your",sub_menu,"is",sum,"Baht.")
    elif sub == "C" or sub == "c" :
        sub_menu = "Cheese Burger"
        sum = 75
        print("Your",sub_menu,"is",sum,"Baht.")
    elif sub == "D" or sub == "d" :
        sub_menu = "Double Cheese Burger"
        sum = 90
        print("Your",sub_menu,"is",sum,"Baht.")
    else:
        print("Invalid sub menu choice.")    
elif main == "C" or main == "c":
    print("---<< Chicken Sub Menu >>---")
    print("%19s"%"<F>ried Chicken")
    print("%21s"%"<G>rilled Chicken")
    print("%20s"%"<C>hef's Chicken")    
    sub = input("Enter your choice: ")
    if sub == "F" or sub == "f" :
        sub_menu = "Fried Chicken"
        sum = 120
        print("Your",sub_menu,"is",sum,"Baht.")
    elif sub == "G" or sub == "g" :
        sub_menu = "Grilled Chicken"
        sum = 150
        print("Your",sub_menu,"is",sum,"Baht.")
    elif sub == "C" or sub == "c" :
        sub_menu = "Chef's Chicken"
        sum = 180
        print("Your",sub_menu,"is",sum,"Baht.")
    else:
        print("Invalid sub menu choice.")          
elif main == "P" or main == "p" :
    print("---<< Pasta Sub Menu >>---")
    print("%27s"%"<S>paghetti de Italiano")
    print("%21s"%"<L>asagna Supreme")
    print("%22s"%"<M>acaroni Special")    
    sub = input("Enter your choice: ")     
    if sub == "S" or sub == "s" :
        sub_menu = "Spaghetti de Italiano"
        sum = 90
        print("Your",sub_menu,"is",sum,"Baht.")
    elif sub == "L" or sub == "l" :
        sub_menu = "Lasagna Supreme"
        sum = 120
        print("Your",sub_menu,"is",sum,"Baht.")
    elif sub == "M" or sub == "m" :
        sub_menu = "Macaroni Special"
        sum = 100
        print("Your",sub_menu,"is",sum,"Baht.")
    else:
        print("Invalid sub menu choice.")    
else:
    print("Invalid main menu choice.")
