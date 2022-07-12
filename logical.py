# def prime(number):
#     i=1
#     count=0
#     while i<len(number):
#         if number[i]%i==0:
#             count=count+1
#         i=i+1
#     if count==2:
#         print(number[i],"is prime")
#     else:
#         print(number[i],"is not prime")
# prime([23,24,25,65,45,7,3,11,71,4])


# l=[23,24,25,65,45,7,3,11,71,4]
# i=1
# l1=[]
# count=0
# while i<len(l):
#     if l[i]%i==0:
#         count=count+1
#     i=i+1


# num=int(input("enter the starting num:-"))
# num1=int(input("enter the lasting num"))
# l=[]
# while num<=(num1):
#         j=1
#         count=0
#         while j<num:
#             if num%j==0:
#                 count=count+1
#             j=j+1
#         if count==1:
#             l.append(num)
#         num=num+1
# print(l)


num=int(input("enter the starting num:-"))
num1=int(input("enter the lasting num"))
l=[]
while num<=(num1):
        j=1
        count=0
        while j<num:
            if num%j==0:
                count=count+1
            j=j+1
        if count==1:
            l.append(num)
            k=1
            while k<len(l):
                print(l[-k],end=" ")
                k=k+1
        num=num+1
print(l)


# a="manpreet"
# b=2.7
# c=2
# d=int(b)
# e=(c+d)
# f=str(e)
# print('"'+a+f+'"')