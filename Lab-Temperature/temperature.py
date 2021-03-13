C = float(input())
Input1 = input()
if Input1 == "F" or Input1 == "f" :
    F = 9/5*C +32
    print(F)
elif Input1 == "K" or Input1 == "k" :
    K = C +273.15
    print(K)
else:
    print("ERROR")