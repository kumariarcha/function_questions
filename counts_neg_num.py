def max():
    list=[-2,-3,-4,-5,-1,-2,-9,-7,-2,-1,-1]
    i=0
    max=list[0]
    count=0
    while i<len(list):
        if list[i]>max:
            max=list[i]
        i=i+1
    j=0
    while j<len(list):
        if max==list[j]:
            count=count+1
        j=j+1
    print(max,count)
max()
