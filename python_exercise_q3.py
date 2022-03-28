# def multiply(numbers):  
#     total = 1
#     i=0
#     while i<len(numbers):
#         total=total*numbers[i]
#         i=i+1
#     return total  
# print(multiply((8, 2,3,-1,7)))





# def test_range(n):
#     if n in range(3,9):
#         print( " %s is in the range"%str(n))
#     else :
#         print("The number is outside the given range.")
# test_range(5)



# def people_with_age_drink(age):
#     if age >= 21:
#         return "drink whisky"
#     elif age >= 18:
#         return "drink beer"
#     elif age >= 14:
#         return "drink coke"
#     else:
#         return "drink toddy"
# print(people_with_age_drink(21))
# print(people_with_age_drink(18))
# print(people_with_age_drink(14))



# x = [4, 6, 8, 24, 12, 2]
# y=sorted(x)
# print(y)
# print(y[len(y)-1])



# def calculate(a,b):
#     return a+b,a-b       
# res = calculate(40,10)
# print(*res,sep=',')




def showEmployee(name, salary):
    default = 9000
    if salary == "": 
        print("Employee:", name, "Default salary is:", default)
    else:
      print("Employee:", name, "salary is:", int(salary))

giveName = input("What's your name? ")
giveSal = input("What's your salary? ")
showEmployee(giveName, giveSal)