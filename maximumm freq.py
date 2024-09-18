num="stringg"
freq={}
for char in num:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)

res=max(freq,key=freq.get)
print(res)
