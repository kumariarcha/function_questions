# list1 = [1, 342, 75, 23, 98]
# list2 = [75, 23, 98, 12, 78, 10, 1]
# i=0
# a=[]
# while i<len(list1):
#     if list1[i] in list2:
#         a.append(list1[i])
#     i=i+1
# print(a)

    
# def common():
#     list1 = [1, 342, 75, 23, 98]
#     list2 = [75, 23, 98, 12, 78, 10, 1]
#     i=0
#     a=[]
#     while i<len(list1):
#         if list1[i] in list2:
#             a.append(list1[i])
#         i=i+1
#     print(a)
# common()


# list1 = [1, 5, 10, 12, 16, 20]
# list2 = [1, 2, 10, 13, 16]
# i=0
# a=[]
# while i<len(list1):
#     if list1[i] in list2:
#         a.append(list1[i])
#     i=i+1
# print(a)




# x = 4234
# x_digits = list(str(x))
# print(x_digits)

# def empty():
#     x=12345
#     a=list(str(x))
#     print(a)
# empty()



# def big():
#     big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
#     counter1 = 0
#     while counter1 < len(big_list):
#         small_list_length = len(big_list[counter1])
#         counter2 = 0
#         while counter2 < small_list_length:
#             print (big_list[counter1][counter2])
#             counter2 = counter2 + 1
#         counter1 = counter1 + 1
#         print ('-----')
# big()


# words = "navgurukul is great"
# counter = 0
# while counter < len(words):
#     print (words[counter],end=" ")
#     counter=counter+1


# def string():
#     sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
#     i=0
#     list=[]
#     str2=" "
#     while i<len(sentence):
#         if sentence[i]==" ":
#             list.append(str2)
#             str2=""
#             i=i+1
#             continue
#         else:
#             str2=str2+sentence[i]
#         i=i+1
#     list.append(str2)
#     print(list)
# string()