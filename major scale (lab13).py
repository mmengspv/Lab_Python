scale = input()
n = int(input())
scale = scale.split(",")
ls = []
for i in scale :
    if i not in ls :
        ls.append(i)
if n%8 == 0 :
    index = 0
elif n > 8 :
    index = (n%7)-1
elif n <= 8 and n > 0  :
    index = n-1
print(ls[index])