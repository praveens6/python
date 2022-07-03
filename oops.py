n=int(input('n: '))
class number:
    def __init__(self,n):
        if n>1:
            for i in range(2,n):
                if n%i==0: #and n%n==1:
                    print(f'{n} is not prime')
                    break
                else:
                    print(f'{n} is prime')
                    break
        else:
            print('enter the number greater than 1')
        
num=number(n)