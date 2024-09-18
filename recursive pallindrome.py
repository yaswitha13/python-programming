num=int(input("enter the string:"))
def reverse(num):
    if num<10:
        return num
    else:
        return int(str(num%10)+str(reverse(num//10)))
def ispallindrome(num):
    if num==reverse(num):
        return 1
    return 0
if ispallindrome(num)==1:
    print("pallindrome")
else:
    print("not a pallindrme")
    
