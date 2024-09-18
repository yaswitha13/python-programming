str1="helloworld"
dict={}

for n in str1:
    keys=dict.keys()
    if n in keys:
        dict[n]+=1
    else:
        dict[n]=1
r=sorted(dict.items(),key=lambda x:x[1])
print(r[-2])
