money = input()
ls1 = []
ls2 = []
error = 0
ls2 = money.split(".")
if "," in money :
    ls1 = ls2[0].split(",")
    if len(ls1[0]) > 3 :
        error += 1
    for i in range(1,len(ls1)) :
        if len(ls1[i]) != 3 :
            error += 1
    for i in ls1 :
        if not i.isdigit() :
            error += 1
            break
    if len(ls2) == 2 :
        ls2 = ["".join(ls1),ls2[1]]
if "." in money :
    if len(ls2[1]) != 2 :
        error += 1
    for i in ls2 :
        if not i.isdigit() :
            error += 1
            break
if error > 0 :
    print("ERROR")
elif "." in money :
    print(float(".".join(ls2))+1)
elif "," in money :
    print(int("".join(ls1))+1)
else :
    print(int(money)+1)