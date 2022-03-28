def numbers(user):
    i=0
    sum=0
    while i<=user:
        if i%3==0 or i%5==0:
            sum=sum+i
        i=i+1
    print(sum)
numbers(10)