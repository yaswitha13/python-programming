num=int(input("enter the number:"))
x=num
sum=0

while num!=1 and num!=4:
    sum=0
    while num>0:
        digit=num%10
        sum+=digit*digit
        num//=10
    num=sum

if(num==1):
    print("happy number")
else:
    print("not a happy number")
    
