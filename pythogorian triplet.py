num=int(input("enter the number:"))
for i in range(1,num+1):
    for j in range(i,num+1):
        for k in range(j,num+1):
            if i**2+j**2==k**2:
                print("pythogorian triplter is:",{i},{j},{k})
