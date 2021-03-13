amount = int(input())
if 0 < amount :
    sum = 0
    time = 1
    count = 0
    while 0 <= time <= amount :
        score = float(input())
        if 40 <= score :
            count += 1        
            time += 1
            sum += score
        elif 0 < score < 40 :
            time += 1
            sum += score             
    xbar = sum/amount
    print("%.2f"%xbar,end=',')
    print(count)
