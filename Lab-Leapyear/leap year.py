year = int(input("Enter year: "))
if year < 0 or year == 0 :
    print("Invalid year.")
elif year%4 == 0 and year%100 != 0 :
    print(year,"is a leap year.")
elif year%4 == 0 and year%100 == 0 and year%400 != 0 :
    print(year,"is not a leap year.")
elif year%4 != 0 :
    print(year,"is not a leap year.")
elif year%400 == 0 :
    print(year,"is a leap year.")