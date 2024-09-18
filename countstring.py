
ucount=0
lcount=0
dcount=0

while True:
    char=input()
    if char=="*":
        break
    if char.isupper():
        ucount+=1
    elif char.islower():
        lcount+=1
    elif char.isdigit():
        dcount+=1
print("the number of upper case are:",ucount)
print("the number of lower count are:",lcount)
print("the  number of digits are:",dcount)
