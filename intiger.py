def inti():
    l=["a","b",2,4,"f","s",5]
    i=0
    while i<len(l):
        if type(l[i])==int:
            print(True)
        else:
            print(False)
        i=i+1
inti()