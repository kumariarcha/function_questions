def greet(*names):
    i=0
    while i<len(names):
        print("Hello", names[i])
        i=i+1
greet("sonu", "kartik", "umesh", "bijender")



# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number/=10
#     return sum

# print(sumofdigits(123))


# def test(x = 1, y = 2):
#     x = x + y
#     y += 1
#     print(x, y)

# test(y = 2, x = 1)