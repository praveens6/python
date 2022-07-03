


import re


class hcf:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def hcf_num(self):
        a=self.a
        b=self.b
        c=[]
        
        for i in range(1,a):
            if a%i==0 and b%i==0:
                c.append(i)
        d=c.pop()
        return d

h=hcf(int(input('a: ')),int(input('b: ')))
print(h.hcf_num())
