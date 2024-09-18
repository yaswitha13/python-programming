
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))


if(n1>n2):
    smaller=n2
else:
    smaller=n1

for i in range(1,smaller+1):
    if(n1%i==0 & n2%i==0):
        hcf=i
print(hcf)
