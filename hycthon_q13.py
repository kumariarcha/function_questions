num= [0,1,0,3,12]
i=0
b=[]
c=[]
while i<len(num):
    if num[i]==0:
        b.append(num[i])
    else:
        c.append(num[i])
    i=i+1
print(c+b)