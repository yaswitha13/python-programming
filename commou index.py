a=input("enter the strning:")
b=input("enter the string:")
count=0
for i in range(min(len(a),len(b))):
    if(a[i]==b[i]):
        count+=1

print(count)
