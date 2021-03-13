inn = input()
inn = inn.lower()
ls = []
i = 0
while i < (len(inn)-1) :
    if inn[i:i+2] not in ls :
        ls.append(inn[i:i+2])
    i += 1
ls.sort()
for i in ls :
    print(i)