n=9
val=1
for i in range(n):
    for j in range(n):
        if i+j>=n-1 and i<=j:
            print(val,end=' ')
            val+=1
            if val>9:
                val=1
        else:
            print(' ',end=' ')
    print()