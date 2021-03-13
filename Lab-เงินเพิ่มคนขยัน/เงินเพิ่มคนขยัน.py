age = int(input("Enter your age: "))
net_income = int(input("Enter your net income: "))
if age < 15 or age > 60 :
    print("Invalid age.")
elif net_income < 0 or net_income >= 80000 :
    print("Invalid income.")
elif 15 <= age <= 60 :
    if 1 <= net_income <= 30000 :
        tax = net_income*20/100
        print("Your negative income tax is %.2f"%tax,"Baht.")
    elif 30000 < net_income < 80000 :
        tax = (net_income*20/100) - (net_income-30000)*(32/100)
        print("Your negative income tax is %.2f"%tax,"Baht.")