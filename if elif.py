def 
C =  float(input())
Input_1 = input()
# = 9/5*C + 32
#= C + 273.15
if  Input_1 =="F" or "f" :
    F = 9/5*C + 32
    print(F)
elif Input_1 == "K" or "k" :
    K = C + 273.15
    print(K)
else:
    print("ERROR")