def even():
    list=[1,2,3,4,5,6,7,8,9,10]
    i=1
    l=[]
    while i<len(list)+1:
        if i%2==0:
            l.append(i)
        i=i+1
    print(l)
even()
