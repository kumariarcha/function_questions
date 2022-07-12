# def even():
#     i=1
#     l=[]
#     while i<=10:
#         l.append(i)
#         i=i+1
#     return l
# def main():
#     a=even()
#     j=0
#     while j<len(a):
#         if a[j]%2==0:
#             print(a[j],"is even num")
#         else:
#             print(a[j],"is odd num")
#         j=j+1
# main()




# def split():
#     string = "my name is archana"
#     i=0
#     list=[]
#     str2=" "
#     while i<len(string):
#         if string[i]==" ":
#             list.append(str2)
#             str2=""
#             i=i+1
#             continue
#         else:
#             str2=str2+string[i]
#         i=i+1
#     list.append(str2)
#     print(list)
# split()


# def split():
#     string="my name is archana"
#     print(len(string))
#     i=0
#     list=[]
#     str2=" "
#     while i<len(string):
#         if string[i]==0:
#             list.append(str2)
#             str2=""
#             i=i+1
#             continue
#         else:
#             str2=str2+string[i]
#         i=i+1
#     list.append(str2)
#     print(list)
# split()  

# def add(a,b):
#     add=a+b
#     print(add)
# def sub(a,b):
#     sub=a-b
#     print(sub)
# def mul(a,b):
#     mul=a*b
#     print(mul)
# def div(a,b):
#     div=a%b
#     print(div)
# def modil(a,b):
#     modil=a//b
#     print(modil)
# def cal(n,n1,n2):
#     if n2=="+":
#         return add(n,n1)
#     elif n2=="-":
#         return sub(n,n1)
#     elif n2=="*":
#         return mul(n,n1)
#     elif n2=="%":
#         return mul(n,n1)
#     elif n2=="//":
#         return modil(n,n1)
# n=int(input("enter the num"))
# n1=int(input("enter the num"))
# n2=(input("enter the operator"))
# cal(n,n1,n2)



# def sum():
#     def sum1(a,b):
#         c=a+b
#         return c
#     return(sum1(4,6))
# print(sum())


# def sum(a=5,b=10):
#     c=a+b
#     def sum1():
#         print(c)
#     sum1()
# sum()


# def greeting(name):
#     print(f"Hello, {name}")
# greeting('Ayushi')




def upper():
    string="MY Name Is Archana Singh"
    upper=0
    lower=0
    i=0
    while i<len(string):
        if string[i].isupper():
            upper=upper+1
        elif string[i].islower():
            lower=lower+1
        else:
            pass
        i=i+1
    print(upper,"upper")
    print(lower,"lower")
upper()