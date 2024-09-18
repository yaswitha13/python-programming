str1=input("enter the string 1:")
str2=input("enter the string 2:")
s=set(str1) and set(str2)
print("the common characters are:")
for i in s:
    print(i)
