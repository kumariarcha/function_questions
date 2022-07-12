def my(user):
    i=0
    a=[]
    while i<len(user):
        if user[i]==user[0]:
            a.append(user[i])
        i=i+1
    if user==a:
        print(True)
    else:
        print(False)
my([1,1,1,1,1,])
