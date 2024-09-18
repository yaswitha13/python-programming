a=[[1,2,3],[4,5,6],[7,8,9]]
print(a)
rcount=[0]*len(a)
ccount=[0]*len(a[0])
dcount=0

for i in range(len(a)):
    for j in range(len(a[0])):
        rcount[i]+=a[i][j]
        ccount[j]+=a[i][j]
    if i==j:
        dcount+=a[i][j]

print("the diagonal count is :",dcount)
print("the row count is :",rcount)
print("the coloumn count is :",ccount)
