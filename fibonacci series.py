n=int(input("enter the number:"))
fib1=0
fib2=1
if n<0:
    print("enter the valid number")
else:
    if n==0:
        print(fib1)
    elif n==1:
        print(fib2)
    else:
        for i in range(2,n):
            fib3=fib1+fib2
            fib1,fib2=fib2,fib3
print(fib3)
