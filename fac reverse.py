import math
num = int(input())
i = num
while True :
    if i < 0 :
        break
    if i <= num :
        j = 1
        print("%d! = %d "%(i,i),end="")
        while True :
            if j >= i :
                break
            print("x %d "%(i-j),end="")
            j += 1
    if i == num :
        summ = math.factorial(num)
        k = num
    if i > 0 and i < num :
        summ = summ/k 
        k -= 1
    print("= %d"%summ)
    i -= 1
