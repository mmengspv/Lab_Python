count = 0
while True :
    pitch1 = int(input())
    pitch2 = int(input()) 
    total = pitch1+pitch2
    print(total)
    
    if pitch1 <= 0 or pitch1 > 6 or pitch2 <= 0 or pitch2 > 6 :
        print("ERROR")
    elif count == 1 and (total == 7 or total == 11) :
        print("1",total,"W")
        break
    elif count == 1 and (total == 2 or total == 3 or total == 12 ) :
        print("1",total,"L")
        
    elif count == 1 and (total == 4 or total == 5 or total == 6 or total == 8 or total == 9 or total == 10) :
        
       
        
    
    