first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
a = first
b = second
print("  >> gcd(%d, %d) ="%(first,second),end="")
while True :
    if second < 1 :
        break
    x = first%second
    first = second
    second = x
print("%7d"%first)
lcm = (a*b)/first
print("  >> lcm(%d, %d) ="%(a,b),end="")
print("%7d"%int(lcm))