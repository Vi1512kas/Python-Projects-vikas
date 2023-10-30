# def operation(**kwargs):
#     print(kwargs)
#     print(type(kwargs))  # dictionary form
#
#
# operation(vikas=20, mohit=40)


# def operation(*args):
#     sum = 0
#     for i in args:
#         sum+=i
#     return sum
#
#
# print(operation(10, 20, 30, 40, 50))   # 150
# print(operation(10, 20))


def operation(n,**kwargs): # n = 10
    n += kwargs["add"]  # n+20 = 10 + 20 = 30
    n *= kwargs["mul"]  # n*40 = 30*40 = 1200
    return n


print(operation(10, add=20, mul=40))