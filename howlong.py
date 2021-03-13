Time = int(input("How many seconds have passed? "))
Timesec = Time%60
Timemin = (Time//60)%60
Timehour = Time//3600
print(Timehour,"hour(s)",Timemin,"minute(s) and",Timesec,"second(s) have passed.")