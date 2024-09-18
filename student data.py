m1=float(input("enter the marks:"))
m2=float(input("enter the marks:"))
m3=float(input("enter the marks:"))
m4=float(input("enter the marks:"))
m5=float(input("enter the marks:"))
total=m1+m2+m3+m4+m5
per=(total/500)*100

if(per>=90):
    grade=print("A")
elif(per>=80):
    grade=print("B")
elif(per>=70):
    grade=print("C")
else:
    grade=print("F")


print(total)
print(per)

