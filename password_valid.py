s=input('enter your password: ')
for i in s:
    if (ord('a')<=ord(i)<=ord('z')) and (ord('A')<=ord(i)<=ord('Z')):
        if len(s)>6:
            print('true')
        else:
            print('false')
            
