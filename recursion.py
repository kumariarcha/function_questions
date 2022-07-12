# def recursion(num,num1):
#     i=1
#     sum=0
#     while i<=num1:
#         if i%num==0:
#             sum+=i
#         i=i+1
#     return sum
# num=int(input("enter the num:-"))
# num1=int(input("enter the num"))
# print(recursion(num,num1))


def inti():
    l=["a","b",2,4,"f","s",5]
    i=0
    while i<len(l):
        if type(l[i])==int:
            print(True)
        else:
            print(False)
        i=i+1
inti()

