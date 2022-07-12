def max():
    list=[1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]
    i=0
    sum=0
    max=0
    while i<len(list):
        if list[i]>max:
            max=list[i]
        if list[i]<0:
            sum=sum+list[i]
            a=[max,sum]
        i=i+1
    print(a)
max()

# def sum(a=5,b=7):
#     c=a+b
#     def sum1():
#         print(c)
#     sum1()
# sum()


# def sum():
    
#     def sum1(a,b):
#         c=a+b
#         return c
#     a=(sum1(4,5))
#     return a
# print(sum())


# def fun():
#     def fun1():
#         print("my fun")
#     print("my function")
#     fun1()
# fun()


