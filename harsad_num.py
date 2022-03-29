def fun():
    s=int(input("enter the number:-"))
    a=s
    rem=0
    sum=0
    while a>0:
        rem=s%10
        sum=sum+rem
        a=a//10
    if s%sum==0:
        print("this is harsad num")
    else:
        print("this is not harsad num")
fun()
    