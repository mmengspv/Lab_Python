import  math
kilometer = int(input())
oil = int(input())
car_kaew = (((kilometer/15)/oil)/0.5) 
car_kaew2 = math.ceil(car_kaew)
if (((kilometer/15)/oil)%0.5) == 0:
    car_kaew2 = car_kaew2 +1
car_khwan = (((kilometer/15)/oil)/0.9) 
car_khwan2 = math.ceil(car_khwan)
if (((kilometer/15)/oil)%0.9) == 0:
    car_khwan2 = car_khwan2 +1
print(car_kaew2)
print(car_khwan2)