# def table():
#     n=int(input("enter the number"))
#     i=1
#     j=5
#     while i<=n:
#         print(i,"*",j,"=",i*j)
#         i=i+1
# table()



def is_divide_by(number, a, b):
    if number % a ==0 and number % b ==0:
        return True
    else:
        return False
print(is_divide_by(10,2,2))