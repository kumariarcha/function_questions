def phone_num():
    a=([8,6,0,3,3,9,4,8,8,6])
    b=""
    c=""
    d="-"
    i=0
    while i<len(a):
        if i<3:
            b=b+str(a[i])
        if i>=3 and i<=5:
            c=c+str(a[i])
        if  i>=6:
            d=d+str(a[i])
        i=i+1
    y="("+b+")"
    print(y+c+d)
phone_num()