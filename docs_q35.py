
# def power(x, y):  
#     if (y == 0): 
#         return 1
#     elif (int(y % 2) == 0):
#         return (power(x, int(y / 2)) *
#             power(x, int(y / 2)))
#     else:
#         return (x * power(x, int(y / 2)) *
#             power(x, int(y / 2)))
# x = 2; y = 3
# print(power(x, ;y))




# def people_with_age_drink(age):
#     if age >= 21:
#         return "drink whisky"
#     elif age >= 18:
#         return "drink beer"
#     elif age >= 14:
#         return "drink coke"
#     elif age>=13:
#         return "drink toddy"
#     else:
#         return "drink anything"
# print(people_with_age_drink(21))
# print(people_with_age_drink(18))
# print(people_with_age_drink(14))
# print(people_with_age_drink(13))


# def couler():
#     lst1 = ['0', '1', '2', '3', '4']
#     lst2 = ['red', 'green', 'black', 'blue', 'white']
#     lst3 = ['100', '200', '300', '400', '500']
#     new_lst = []
#     i=0
#     while i<len(lst1):
#         if len(lst1) == len(lst2) == len(lst3):
#             new_lst.append(lst1[i] + lst2[i] + lst3[i])
#         else:
#             print("All list should have same number of elements!")
#         i=i+1
#     print(new_lst)
# couler()



# list=['a','b','b','c','c','d','e','e','e','f','g'] 
# i=0
# a=" "
# while i<len(list)-1:
#     if list[i]!=list[i+1]:
#         a=a+list[i]
#     i=i+1
# a=a+list[i]
# print(a)

# list=["a","b","c","c","c","d","e","f","g"]
# i=0
# a=" "
# while i<len(list)-1:
#     if list[i]!=list[i+1]:
#         a=a+list[i]
#     i=i+1
# a=a+list[i]
# print(a)


# def comb(L): 
#     for i in range(3):
#         for j in range(3):
#             for k in range(3):
#                 if (i!=j and j!=k and i!=k):
#                     print(L[i], L[j], L[k])
# comb([1, 2, 3])




# def comb(l):
#     i=0
#     while i<len(l):
#         j=0
#         while j<i:
#             k=0
#             while k<i:
#                 if (l[i]!=l[j] and l[j]!=l[k] and l[i]!=l[k]):
#                     print(l[i],l[j],l[k])
#                 k=k+1
#             j=j+1
#         i=i+1
# comb([1,2,3])
                


n=[1,1,1,2,2,2,3,4,4,4,5,5,5,6,6]
i=0
while i<len(n)-2:
    if n[i]==n[i+1] and n[i+1]==n[i+2]:
        print(n[i])
    i=i+1