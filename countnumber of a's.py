string="hello wrold"
count=0
a=string.upper()
for i in string:
    if i.startswith("l"):
        count+=1
print("the capital strnig is :",a)
print("number of l's are:",count)
