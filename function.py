import math
x = float(input("Enter x : "))
if x < 0 :
    sum = math.sqrt(x**2+1)
    print("f(%.2f)"% x ,"=", math.ceil(sum))
elif x == 0 :
    sum = x
    print("f(%.2f)"% x ,"=", math.ceil(sum))
elif 0 < x <= 99 :
    sum = (3*x**2)-((1-x)**2)
    print("f(%.2f)"% x ,"=", math.ceil(sum))
elif x > 99 :
    sum = (2*x**3)-(x/(math.sqrt(x+1)))
    print("f(%.2f)"% x ,"=", math.ceil(sum))