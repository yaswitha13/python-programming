arr=[1,2,3,4,-6,-3,-8,-4,-10,-45,-78]
positive=0
negative=0

for i in arr:
    if i>0:
        positive+=1
    elif i<0:
        negative+=1
        
print("number of positive numbers are:",positive)
print("number of negative numbers are:",negative)
