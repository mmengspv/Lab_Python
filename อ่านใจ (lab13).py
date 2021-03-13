t1 = input()
t2 = input()
l1 = []
l2 = []
l3 = []
p = b = 0
for i in range(len(t1)):
    l1.append(t1[i])
for i in range(len(t2)):
    l2.append(t2[i])
i = len(l1)-1
j = len(l2)-1
if i>j:
    a = i
    l3.extend(l1)
    l1.clear()
    i = j
    l1.extend(l2)
    l2.clear()
    j = i
    l2.extend(l3)
    l3.clear()
k1 = k2 = 0
while k1 <= i and k2 <= j:
    if l1[k1] == l2[k2]:
        p += 1
        l1.pop(k1)
        l2.pop(k2)
        l1.insert(k1," ")
        l2.insert(k2," ")
    k1 += 1
    k2 += 1
k1 = k2 = 0
while k1 <= i:
    while k2 <= j:
        if l1[k1] == l2[k2]:
            if l1[k1]!=" " and l2[k2]!=" ":
                b += 1
                l1.pop(k1)
                l2.pop(k2)
                l1.insert(k1, " ")
                l2.insert(k2, " ")
        k2 += 1
    k2 = 0
    k1 += 1
print(str(p)+"-"+str(b))