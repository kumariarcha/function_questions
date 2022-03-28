
def square(num):
    a=[]
    i=1
    while i<=num:
        a.append(i*i)
        i=i+1
    j=1
    b=[]
    while j<len(a):
        c=a[0:5:1]
        d=a[-5:-1]
        j=j+1
    b.append(c)
    b.append(d)
    print(b)
square(30)