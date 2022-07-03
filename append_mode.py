a=open('file1.txt','a+')
print(a)
a.write('\nlucifer')
l='\nready to fire\ngo with flow'
a.writelines(l)
if a.readable():
    print('readable')
else:
    print('not readable')
if a.writable():
    print('writable')
else:
    print('not writable')
a.close()
