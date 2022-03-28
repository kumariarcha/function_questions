def check_range(first,last,number):
    if number in range (first,last):
        print(number, "is in range")
    else:
        print(number,"is not in range")
first=int(input("enter the start range"))
last=int(input("enter the end range"))
number=int(input("enter the num"))
check_range(first,last,number)

# def sum():
#     a=(input("enter the num"))
#     n=str(a)
#     i=0
#     sum=0
#     while i<len(n):
#         sum=sum+int(n[i])
#         i=i+1
#     if sum%2==0:
#         print(sum,"is even")
#     else:
#         print(sum,"is odd")
# sum()