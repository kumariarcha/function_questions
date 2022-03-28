def remove_zero(number):
    if number%10==0:
        print(number//10)
    else:
        print("number does not end with zero")
number=int(input("enter the num:-"))
remove_zero(number)