num = int(input("Enter a number: "))
i = 0
j = 1
k = 0
summ = 1
if num < 0 :
    print("Invalid input, program terminates.")
else :
    while True :
        if i > num :
            break
        if i <= 1 :
            print("%d! = 1 = 1"%i)
        else :
            while j < i:
                summ = summ*i
                print("%d! ="%i,"%d"%i,end="")
                while i > 1 :
                    k = i-1
                    i -= 1
                    print(" x %d"%k,end="")
                print(" = %d "%summ,end="")
                print(end="\n")
                j += 1
        i += 1
        
        

