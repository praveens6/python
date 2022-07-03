s=open('file1.txt','w+')
print(s)
s.write('ghost rider\n')
print(s.tell())
l=['thunder bolt\n','pirates\n','india']
s.writelines(l)
s.seek(0)
s.read(5)
print(s.tell())
l1=[]
for i in l:
    l1.append(i.rstrip('\n'))
print(s.readlines())
print(l1)
print(s.tell())
if s.writable():
    print('file is writable')
else:
    print('file is not writable')
s.close()