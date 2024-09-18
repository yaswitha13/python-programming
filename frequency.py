item_list="hello"
frequency={}
for items in item_list:
    if items in frequency:
        frequency[items]+=1
    else:
        frequency[items]=1
print(frequency)
