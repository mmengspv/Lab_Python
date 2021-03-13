inn = input()
inn = inn.lower()
count = 0
for i in inn :
    if count == 0 :
        maxx = i
        count +=1
    elif count > 0 :
        if i > maxx :
            maxx = i
            count +=1
        else :
            break 
print(count)