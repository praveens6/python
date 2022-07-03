n=9474
a=n
sum=0
c=0
while n>0:
    n//=10
    c+=1
n=a
while n>0:
    rem=n%10
    sum=sum+rem**c
    n//=10
if a==sum:
    print(True)
else:
    print(False)

