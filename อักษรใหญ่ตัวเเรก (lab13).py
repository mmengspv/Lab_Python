inn = input()
inn = inn.split(" ")
check = ["for","and","with","of"]
x = []
for i in inn :
    if i in check :
        x.append(i)
    else :
        x .append(i.title())
print(" ".join(x))