min = int(input("Minutes before due: "))
Tem = float(input("Temperature: "))
rain = input("Is it raining (y/n)? ")
day = int(min/1440)+((min//720)%2)
print(">>>",day,"days before due.")
if day < 2 :
    print(">>> I will do the assignment.")
elif day > 5 :
    print(">>> I will not do the assignment.")
elif Tem > 40 or ( Tem > 25 and (rain == "Y" or rain == "y" ) ) :
    print(">>> I will not do the assignment.")
elif Tem <= 40 or rain == "N" or rain == "n" :
    print(">>> I will do the assignment.")