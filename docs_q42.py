def sum():
    a=[12,67,98,34]
    i=0
    while i<len(a):
        b=str(a[i])
        j=0
        sum=0
        while j<len(b):
            sum=sum+int(b[j])
            j=j+1
        print(sum,end=" ")
        i=i+1
sum()
