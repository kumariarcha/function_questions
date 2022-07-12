def mul(a,b):
    multiple=a*b
    print(multiple)
def add(a,b):
    addition=a+b
    print(addition)
def sub(a,b):
    subtraction=a-b
    print(subtraction)
def expo(a,b):
    exponent=a**b
    print(exponent)
def divi(a,b):
    divisible=a/b
    print(divisible)
def flo(a,b):
    flordivision=a//b
    print(flordivision)
def mudo(a,b):
    mudolas=a%b
    print(mudolas)
def main(n,num,num1):
    if num1=="*":
        return mul(n,num)
    elif num1=="+":
        return add(n,num)
    elif num1=="-":
        return sub(n,num)
    elif num1=="**":
        return expo(n,num)
    elif num1=="/":
        return divi(n,num)
    elif num1=="//":
        return flo(n,num)
    elif num1=="%":
        return mudo(n,num)
n=int(input("Enter the numbers:-"))
num=int(input("Enter the numbers:-"))
num1=(input("Enter the opertoras:-"))
main(n,num,num1) 