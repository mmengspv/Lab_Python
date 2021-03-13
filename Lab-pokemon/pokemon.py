level = int(input("Enter level pokemon: "))
pokeball = input("Enter level pokeball: ")
distance = int(input("Enter distance: "))
if (pokeball == "M" or pokeball == "m" ) and 0 <= level <= 40 :
    x = 0.03 
elif (pokeball == "M" or pokeball == "m" ) and 40 < level <= 60 :
    x = 0.05
elif (pokeball == "M" or pokeball == "m" )and 60 < level <= 100 :
    x = 0.08
elif (pokeball == "L" or pokeball == "l" ) and 0 <= level <= 40 :
    x = 0.05 
elif ( pokeball == "L" or pokeball == "l" ) and 40 < level <= 60 :
    x = 0.03
elif ( pokeball == "L" or pokeball == "l" ) and 60 < level <= 100 :
    x = 0.1
elif ( pokeball == "H" or pokeball == "h" ) and 0 <= level <= 100 :
    x = 0.01
sum = 100-(level*distance*x)
if sum <= 0 :
    sum = 0
elif sum >= 100 :
    sum = 100
print("%.2f"%sum,"percent.")   
        