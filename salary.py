# def showEmployee(name, salary):
#     default = 9000
#     if salary == "": 
#         print("Employee:", name, "Default salary is:", default)
#     else:
#       print("Employee:", name, "salary is:", int(salary))

# giveName = input("What's your name? ")
# giveSal = input("What's your salary? ")
# showEmployee(giveName, giveSal)



# def showEmployee(name, salary=9000):
    
#     return name,salary

# print(*showEmployee("Abdu",57887))




# def outerFun(a, b):
#     square = a**2
#     def innerFun(a,b):
#         return a+b
#     add = innerFun(a, b)
#     return add+5

# result = outerFun(5, 10)
# print(result)