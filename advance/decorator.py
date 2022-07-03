# # def my_decorator(fun):
# #     def inner_fun():
# #         print('hi')
# #         fun()
# #         print('bye')
# #     return inner_fun

# # @my_decorator
# # def fun():
# #     print('hello')
    
# # fun()
# number=int(input('enter the value: '))
# sum=0
# mul=1
# alternate=number
# def my_decorator(fun):
#     def inner_fun():
#         global number,sum,mul
#         while number>0:
#             rem=number%10
#             sum=sum+rem
#             mul=rem*mul
#             number=number//10
#         fun()
#     return inner_fun

# @my_decorator
# def fun():
#     if sum+mul==alternate:
#         print('special number')
#     else:
#         print('not special number')
# fun()
# def split_and_join(line):
#     # write your code here
#     return line.replace(' ','-')
# split_and_join('this is my name')

