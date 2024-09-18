num=input("enter the number:")
for i in range(4):
    for j in range(4):
        for k in range(4):
            if i!=j and j!=k and k!=i:
                print(num[i],num[j],num[k])
