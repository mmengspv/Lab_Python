inn1 = input()
inn2 = input()
decode = input()
inn1 = inn1.replace(" ","")
k = ""
for i in inn1 :
    if i not in k :
        k+= i
x = ""
for i in decode :
    if i in inn2 :
        find = inn2.find(i)
        x += k[find]
        inn1.replace(i,"",1)
    else:
        x += i  
print(x)