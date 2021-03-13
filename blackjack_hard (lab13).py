a = ['J','Q','K']
b = j = 0
q = []
s = input()
s = s.upper()
w = s
w = w.replace("10",'t')
r = 0
p = "A23456789tJQK"
l = ''
m = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
s = s.split(" ")
u = 0
for i in range(5):
    if s[i] in m:
        u += 1
if len(s)==5 and u == 5:
    for i in range(5):
        if s[i] == "A":
            s[i] = 1
        elif s[i] in a:
            s[i] = 10
        else:
            s[i] = int(s[i])
    for i in range(5):
        b += s[i]
        r += 1
        if b > 21:
            q.append(0)
            j = 1
            break
        elif b > 16:
            q.append(b)
            j = 1
            break
    if j == 0:
        q.append(b)
    e = 0
    w = w.replace(" ","")
    for i in range(r):
        n = p.find(w[i])
        if n > e:
            e = n
    p = p.replace("t", "10")
    if e == 9:
        print(p[9:11])
    else:
        if e < 9:
            print(p[e])
        else:
            print(p[e + 1])
    for i in range(len(q)):
        if q[i] == 0:
            print("busted")
        else:
            print(q[i])