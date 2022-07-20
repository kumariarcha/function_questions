# def sum(a,b):
#     c=a+b
#     return c
# print(sum(3,5))



# def sum(a=5,b=6):
#     c=a+b
#     return c

# print(sum(9))


# def sum(a=8,b=7):
#     c=a+b
#     return c
# print(sum(9,8))


# def add(a,b=5):
#     c=a+b
#     print(c)
# add(4,6)


# def sum(a,b):
#     c=a+b
#     return c
# def sum1():
#     print(sum(3,4))
# sum1()


# num=int(input("enter the num:-"))
# if num>0:
#     print(num*-1)
# elif num<0:
#     print(num*-1)
# else:
#     print("enter the any num pos ya neg")





# def fun(*args):
    #     print(args)
# fun(10,20,30)



# def add (*args):
#     i=0
#     sum=0
#     while i<len(args):
#         sum=sum+args[i]
#         i=i+1
#     print(sum)
# add(10,20,30,40)



# def fun(**kwargs):
#     if 'Archana' in kwargs['name']:
#         print("found")
#     else:
#         print("not found")
# fun(surname="singh",name="Archana")


# def fun(*args, **kwargs):
#     print(args)
#     print(kwargs)
# fun(3,4,name="archana")


# def fun(*name):
#     print(name)
# fun("archana","swati")


# def fun(**name):
#     print(name)
# fun(name='Archana',sirname='singh')


# def even(n,n1):
#     i=0
#     while i<len(n and n1):
#         if n[i]%2==0 and n1[i]%2==0:
#             print("both are even num")
#         else:
#             print("both are not even")
#         i=i+1
# even([2,3,4,6],[2,4,5,8])




# def perfect():
#     n=int(input("enter the num"))
#     i=1
#     sum=0
#     while i<n:
#         if n%i==0:
#             sum=sum+i
#         i=i+1
#     if sum==n:
#         print(n,"perfect num")
#     else:
#         print(n,"not perfect")
        
# perfect()


# def add():
#     a=[12,23,34,45]
#     i=0
#     while i<len(a):
#         b=str(a[i])
#         j=0
#         sum=0
#         l=[]
#         while j<len(b):
#             sum=sum+int(b[j])
#             j=j+1
#         i=i+1
#         print(sum,end=" ,")
# add()



# def name():
#     n=str(input("enter the name"))
#     i=0
#     c=0
#     d=0
#     while i<len(n):
#         if n[i].isalpha():
#             c=c+1
#         elif n[i].isdigit():
#             d=d+1
#         i=i+1
#     print(c,"alph")
#     print(d,"digit")
# name()


# def upper():
#     n=str(input("enter the name:-"))
#     i=0
#     upper=0
#     lower=0
#     while i<len(n):
#         if n[i].isupper():
#             upper=upper+1
#         elif n[i].islower():
#             lower=lower+1
#         i=i+1
#     print(upper,"upper")
#     print(lower,"lower")
# upper()  

def count():
    list=["a","b","c","a","a","b","c","6","7","6","7","6"]
    n=(input("enter the num:-"))
    i=0
    count=0
    while i<len(list):
        if list[i]==n:
            count=count+1
        i=i+1
    print(count)
count()