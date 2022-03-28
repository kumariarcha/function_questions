# def mathematic():
#     x=int(input("enter the num:-"))
#     y=int(input("enter the num:-"))
#     z=input("enter the num:-")
#     if z=="+":
#         print(x+y)
#     elif z=="-":
#         print(x-y)
#     elif z=="*":
#         print(x*y)
#     elif z=="/":
#         print(x/y)
# mathematic()


# def multipal(num1,num2):
#     i=0
#     while i<len(num1):
#         a=num1[i]*num2[i]
#         i=i+1
#         print(a)
# multipal([5,10,20,50],[2,20,3,5])



# def addEven(n, m):
#     if n%2 == 0 and m%2 == 0:
#         return n+m
#     else:
#         return n*m



# print(addEven(2,2,))
# print(addEven(2,3))


def calcuter(number_x,number_y,op):
    if op=="sum":
        result=number_x+number_y
    elif op=="substract":
        result=number_x-number_y
    elif op=="multiply":
        result=number_x*number_y
    elif op=="divide":
        result=number_x%number_y
    return result
number_1=calcuter(20,24,"sum")
numer_2=calcuter(50,60,"substract")
number_3=calcuter(80,120,"multiply")
number_4=calcuter(90,23,"divide")
print(number_1)
print(numer_2)
print(number_3)
print(number_4)