# a=input("enter the any num:-")
# b=" "
# c=["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
# i=0
# while i<len(a):
#     j=0
#     while j<len(c):
#         if a[i]==str(j):
#             b+=""+c[j]
#         j=j+1
#     i=i+1
# print(b)


# def num():
#     a=input("enter the any num:-")
#     b=" "
#     c=["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
#     i=0
#     while i<len(a):
#         j=0
#         while j<len(c):
#             if a[i]==str(j):
#                 b=b+""+c[j]
#             j=j+1
#         i=i+1
#     print(b)
# num()



a=input("enter the any num:-")
b=" "
c=["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
i=0
while i<len(a):
    j=0
    while j<len(c):
        if a[i]==str(j):
            b=b+""+c[j]
        j=j+1
    i=i+1
print(b)
print(len(a))
print(len(c))

