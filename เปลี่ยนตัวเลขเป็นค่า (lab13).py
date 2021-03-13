inn1 = input()
if len(inn1) <= 3 and inn1.isdigit() and int(inn1) >= 0:
    inn1 = inn1.lstrip("0")
    if inn1 == "" :
        inn1 = "0"
    x = ["one","two","three","four","five","six","seven","eight","nine"]
    ls1 = ["10","ten","11","eleven","12","twelve","13","thirteen","14","fourteen","15","fifteen","16","sixteen","17","seventeen","18","eighteen","19","nineteen","20","twenty","30","thirty","40","forty","50","fifty","60","sixty","70","seventy","80","eighty","90","ninety"]
    ls2 = ["100","one-hundred","200","two-hundred","300","three-hundred","400","four-hundred","500","five-hundred","600","six-hundred","700","seven-hundred","800","eight-hundred","900","nine-hundred"]
    if inn1 == "0" :
        ans = "zero"
    elif len(inn1) == 1 :
        ans = x[int(inn1)-1]
    elif len(inn1) == 2:
        if inn1 in ls1 :
            find = ls1.index(inn1)
            ans = ls1[find+1]
        elif inn1 not in ls1 :
            find = ls1.index(inn1[0]+"0")
            ans = ls1[find+1]+"-"+x[int(inn1[1])-1]
    elif len(inn1) == 3 :
        if inn1 in ls2 :
            find = ls2.index(inn1)
            ans = ls2[find+1]
        elif inn1 not in ls2 and int(inn1[0]) > 0:
            ans = x[int(inn1[0])-1]+"-hundred"
            if inn1[1:] in ls1 :
                find = ls1.index(inn1[1:])
                ans += "-"+ls1[find+1]
            elif inn1[1] == "0" :
                ans += "-"+x[int(inn1[2])-1]
            elif inn1[1] != "0" :
                find = ls1.index(inn1[1]+"0")
                ans += "-"+ls1[find+1]
                ans += "-"+x[int(inn1[2])-1]
    print(ans)
else :
    print("ERROR")