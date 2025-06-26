for x in range(5):
    temp=1
    for y in range(5):
        if x>y:
            print("  ",end="  ")
        else:
            print(temp,end="  ")
            temp=temp+1
    
        
    print()
