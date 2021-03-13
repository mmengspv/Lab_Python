n = int(input())
ls = []
x = ""
k = 0
for i in range(n) :
    inn = input()
    x += inn
    if inn not in ls :
        ls.append(inn)
for i in ls :
    if x.count(i) > (n/2) :
        y = i
        k += 1
        print(y)
if k == 0 :
    print("0")
