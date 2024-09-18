string=str(input("enter the string:"))
letter=0
digit=0
for char in string:
    if char.isalpha():
        letter+=1
    elif char.isdigit():
        digit+=1
print(letter)
print(digit)
