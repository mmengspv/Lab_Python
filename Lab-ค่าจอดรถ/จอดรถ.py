Hour = int(input("Enter number of hours: "))
min = int(input("Enter number of minutes: "))  
if Hour < 0 or min >= 60 or min < 0 :
    print("Input Error!")
elif Hour == 0 and min <= 15 :
    print("No charge, thanks.")
elif Hour < 2 and min > 0 :
    print("Total amount due is 10 Bahts.")
elif Hour >= 2 and min == 0 :
    sum = 10+10*(Hour-2)
    print("Total amount due is",sum,"Bahts.")
elif Hour >= 2 and min > 0 :
    Hour = Hour + 1
    sum = 10+10*(Hour-2)
    print("Total amount due is",sum,"Bahts.")
    
    
    hour = int(input("Enter number of hours: "))
    min = int(input("Enter number of minutes: "))
    if hour < 0 or min > 59 or min < 0:
        print("Input Error!")
    elif hour == 0 and 0 <= min <= 15 :
        print("No charge, thanks.")
    elif hour == 0 and min>15 :
        print("Total amount due is 10 Bahts.")
    elif 0 <= hour < 2 or ( hour == 2 and min == 0 ) :
    elif hour>2 and min == 0 :
        sum = 10*(hour-1)
        print("Total amount due is",sum,"Bahts.")
    elif hour>= 2 and min>0 :
        sum = 10*(hour)
        print("Total amount due is",sum,"Bahts.")