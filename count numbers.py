string=str(input("enter the number"))
digit=0
for char in string:
    if char.isdigit():
        digit+=1
    else:
        print("not digit found")
print(digit)
