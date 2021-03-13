num = int(input())
a = 0
b = num-1
i = 0
k = 0
while True :
    if a >= num-1 :
        break
    b-=1
    print(" "*2*a+"x",end="")
    print(" "*(4*b+3)+"x")
    a += 1

while True :
    if num < 1 :
        break
    if i == 0 :
        print(" "*(num*2-2)+"x")
    elif i > 0 :
        print(" "*(num*2-2)+"x",end="")
        print(" "*(4*k+3)+"x")
        k += 1
    num -= 1
    i += 1 