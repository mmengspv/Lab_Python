day = input()
x = int(input())
if (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday" or day == "Sunday" ) and (x>0 and x <=31 ) :
    if day == "Monday" :
        y = (x-1)%7
    elif day == "Tuesday" :
        y = x%7
    elif day == "Wednesday" :
        y = (x+1)%7
    elif day == "Thursday" :
        y = (x+2)%7
    elif day == "Friday" :
        y = (x+3)%7
    elif day == "Saturday" :
        y = (x+4)%7
    elif day == "Sunday" :
        y = (x+5)%7
        
    if y == 0 :
        print("Monday")
    elif y == 1 :
        print("Tuesday")
    elif y == 2 :
        print("Wednesday")
    elif y == 3 :
        print("Thursday")
    elif y == 4 :
        print("Friday")
    elif y == 5 :
        print("Saturday")
    elif y == 6 :
        print("Sunday")    
else :
    print("ERROR")