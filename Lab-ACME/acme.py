buy = float(input("Enter buying amount: "))
if 0 < buy < 1000 :
    print("Amount due after discount is %.2f"%buy,"baht.")
elif 1000 <= buy < 3000 :
    sum = buy*90/100
    print("Amount due after discount is %.2f"%sum,"baht.")
elif buy >= 3000 :
    sum = buy*85/100
    print("Amount due after discount is %.2f"%sum,"baht.")