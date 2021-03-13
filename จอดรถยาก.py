hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))
buyAmt = int(input("Enter shopping amount: "))
if (hours > 20 or hours < 0) or (hours >= 20 and minutes > 0 ) or (minutes > 59 or minutes < 0) :
    print("Invalid time.")
elif hours < 2 or ( hours == 2 and minutes == 0 ) or buyAmt >= 3001 :
    print("No charge, thank you.")
elif buyAmt >= 300 and buyAmt <= 3000 :
    if hours < 4 or (hours == 4 and minutes == 0 ) : 
        print("No charge, thank you.")
    else :
        if minutes == 0 :
            sum = (hours-4)*50
        else :
            sum = (hours-3)*50
        print("Total amount due is %d Baht, thank you."%sum)
elif buyAmt < 300 :
    if hours < 4 or (hours == 4 and minutes == 0 ) :
        if minutes == 0 :
            sum = (hours-2)*20
        else: 
            sum = (hours-1)*20
    else : 
        if minutes == 0 : 
            sum = 40+(hours-4)*50
        else: 
            sum = 40+(hours-3)*50       
    print("Total amount due is %d Baht, thank you."%sum)
