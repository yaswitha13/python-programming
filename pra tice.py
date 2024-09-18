number = int(input("enter the number:"))
rev = 0

while number != 0:
    digit = number % 10
    rev= rev * 10 + digit
    number //= 10
    
print(rev)
