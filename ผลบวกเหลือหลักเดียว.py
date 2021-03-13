n = int(input())
count = 0
count1 = 0
while True:
    a = n%10
    count = count+a
    n = n//10
    if n//10==0:
        b = count+n
        print(b)
        break
