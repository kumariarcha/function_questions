def fibonacc(num):
    a,b=0,1
    i=0
    while i<=num:
        print(a)
        i=i+1
        a,b=b,a+b
num=int(input("enter the num"))
fibonacc(num)