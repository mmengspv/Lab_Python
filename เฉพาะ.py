height = int(input("Enter height: "))
width = int(input("Enter width: "))
i = 1 
if width <= 0 or height <= 0 :
    print("Invalid input, program terminates.")

while i <= height :
    if i%2 == 1 :
        print("* "*width,end="")
    elif i%2 == 0 :
        print(" *"*width,end="")
    print(end="\n")
    i += 1