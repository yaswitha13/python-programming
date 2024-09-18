string=str(input("enter the string:"))
vcount=0
ccount=0
vowels="aeiouAEIOU"
for char in string:
    if char.isalpha():
        if char in vowels:
            vcount+=1
        else:
            ccount+=1
print("the number of vowels are:",vcount)
print("the number of consonenst are:",ccount)
