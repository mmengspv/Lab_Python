n = []
while True:
    s = int(input())
    if s == 0:
        break
    else:
        n.append(s)
q = e = len(n)-1
w = len(n)-2
a = s = 0
b = n[0]+n[1]
m = 1
for i in range(q):
    for j in range(m):
        k = s
        w += 1
        while k <= w:
            a += n[k]
            k += 1
        if a > b:
            b = a
        a = 0
        s += 1
    m += 1
    e -= 1
    w = e-1
    s = 0
print(b)