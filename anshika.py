# i=0
# def my_function():
#     global i
#     i=i+1
#     print("my function",i)
#     my_function()
# my_function()


# def num():
#     a=2
#     b=3
#     c=num()
#     print(a+b)
# num()

# i=1
# while True:
#     if i<=10:
#         print(i)
#     i=i+1


# def fibonacci(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return(fibonacci(n-1)+fibonacci(n-2))
# print(fibonacci(8))

# a=1
# b=4
# def abc():
#     global a,b
#     c=a+b
#     print("my name",c)
#     abc()
# abc()

# def my_function(*kids):
#       print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus") 



# def my_function(*kids):
#     print(kids[1])
#     my_function()
# my_function("archana","devika","rinki")


# def my_function(country = "Norway"):
#       print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil") 



# def my_function(x):
#       return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9)) 



# def tri_recursion(k):
#     if(k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#         return result
# print("\n\nRecursion Example Results")
# tri_recursion(6)