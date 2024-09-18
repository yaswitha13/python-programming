a=[[1,2,3],[4,5,6],[7,8,9]]
print(a)
list=[]
for i in range(len(a[0])):
    for j in range(len(a[0])):
        list.append(a[i][j])
print(max(list))
