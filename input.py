def user():
    num=int(input("enter the num:-"))
    num1=int(input("enter the num:-"))
    sum=0
    i=num
    a=[]
    if num<0:
        print("invild")
    else:
        while i<=num1:
            if i%3==0:
                sum=sum+i
                a.append(i)
            i=i+1
        print(a)
        print(sum)
user()