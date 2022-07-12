
a=[1,2,3,4,5,6,7,8,9,10,11,54,67,45,17,32]
l=[]
i=0
while i<len(a):
    j=1
    count=0
    while j<a[i]:
        if a[i]%j==0:
            count=count+1
        j=j+1
    if count==1:
        l.append(a[i])
    i=i+1
print(l)

