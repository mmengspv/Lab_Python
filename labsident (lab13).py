import math
damage = int(input())
ls = []
total = 0
hp = input()
hp = hp.split(" ")
for i in hp :
    bullet = (int(i)//damage)
    if int(i)%damage > 0 :
        bullet += 1
    total += bullet
    ls.append(total)
print(total)
for i in ls :
    print(i,end=" ")
    
