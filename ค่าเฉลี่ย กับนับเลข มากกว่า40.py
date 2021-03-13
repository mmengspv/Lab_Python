n = int(input())
i = 1
sum = 0
count = 0
while i <= n :
    score = float(input())
    sum = sum+score
    i += 1
    if 0<= score <= 40 :
        pass
    elif score > 40 :
        count += 1
average = sum/n
print("%.2f"%average,count)

    