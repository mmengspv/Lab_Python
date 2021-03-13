inn = input()
amount = len(inn)
ans = ""
x = inn[:amount//2]
y = inn[amount//2:]
i = 0 
for i in range(amount//2) :
    ans += x[i]+y[len(y)-1-i]
if amount%2 == 0 :
    print(ans)
else :
    print(ans+inn[(amount//2)])