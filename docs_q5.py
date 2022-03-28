def dublicat():
    num=[1,2,3,3,3,4,5]
    i=0
    a=[]
    while i<len(num):
        if num[i] not in a:
            a.append(num[i])
        i=i+1
    print(a)
dublicat()