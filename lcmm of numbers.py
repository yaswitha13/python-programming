x=int(input("enter the number :"))
y=int(input("enter the number 2:"))

if x>y:
    greater=x
else:
    greater=y

while(True):
    if(greater%x==0) and (greater%y==0):
        lcm=greater
        break
    greater+=1
print("the lcm is :",lcm)
