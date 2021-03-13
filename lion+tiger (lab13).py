n1 = input()
n2 = input()
a = ["a","e","i","o","u"]
b = 0
for i in range(len(n1)):
    if n1[i] in a:
        b += 1
    if b == 2:
        n1 = n1[:i]
        break
for i in range(len(n2)):
    if n2[i] in a:
        if i == len(n2)-1:
            break
        n2 = n2[i+1:]
        break
print(n1+n2)