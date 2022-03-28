def sum():
    a=["4","5"]
    a=["34","5"]
    x=[]
    i=0
    sum=0
    while i<len(a):
        sum=sum+int(a[i])
        i=i+1
    x.append(str(sum))
    print(x)
sum()