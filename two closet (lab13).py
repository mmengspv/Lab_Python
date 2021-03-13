import math
n = int(input())
ls = []
for i in range(n) :
    score = int(input())
    ls.append(score)
ls.sort()
j = 0 
diff = math.inf
while j < len(ls)-1 :
    x = ls[j+1]-ls[j]
    if x < diff :
        diff = x
    j += 1
k = 0
ans = []
while k < len(ls)-1 :
    if ls[k+1]-ls[k] == diff :
        ans.append(str(ls[k])+" "+str(ls[k+1]))
    k += 1
for i in ans :
    print(i)