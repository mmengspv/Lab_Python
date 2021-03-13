f0 = 0
f1 = 1
num = int(input())
i = 0 
while True :
    if i >= num :
        break
    if i == 0 :
        print("%d, "%f0,end="")
    elif i == 1:
        print("%d, "%f1,end="")
    elif i > 1 :
        f2 = f1+f0
        f0 = f1
        f1 = f2
        print("%d, "%f2,end="")
    i += 1