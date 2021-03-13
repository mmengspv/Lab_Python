i = 1
sum = 0
while i  :
    n = input()
    if n != "" :
        n = float(n)
        if n >= 0:
            max = 0
            min = 0
            sum = sum + n
            if n > max :
                max = n 
            elif n < min :
                min = n
        average = sum/n
        print("%.2f %.2f"%(max,min))
        print("%.2f %.2f"%(sum,average))