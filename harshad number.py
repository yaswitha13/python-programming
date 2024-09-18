num=int(input("enter the number:"))
n=num
rem=sum=0

while num>0:
    rem=num%10
    sum+=rem
    num//=10
if(n%sum==0):
    print("harshad number")
else:
    print("not a harshad number")
    
