inn = input()
n = int(input())
if n == 0 :
    print(inn)
elif n > 0 :
    x = inn[len(inn)-n:]+inn[:len(inn)-n]
    print(x)
elif n < 0 :
    n = n%len(inn)
    x = inn[-n:]+inn[:-n]
    print(x)
