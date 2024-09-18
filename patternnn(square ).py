rows=int(input("enter the number:"))
x=2
for i in range(rows+1):
    for j in range(i):
        print(x,end=" ")
    x=x*x
    print()
