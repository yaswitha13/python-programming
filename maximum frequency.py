string="hello world"
frequency={}
for items in string:
    if items in frequency:
        frequency[items]+=1
    else:
        frequency[items]=1
max_freq=max(frequency,key=frequency.get)
print(max_freq)
