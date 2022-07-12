def add():
    list=[[1,2,3],[4,5,6],[7,8,9]]
    i=0
    while i<len(list):
        j=0
        list2=[]
        while j<len(list[i]):
            list2.append(sum(list[j]))
            j=j+1
        i=i+1
    print(list2)
add()

