def count():
    a=['a','b','b','b','a','1','5','5','a']
    user=input("enter the num:-")
    i=0
    count=0
    while i<len(a):
        if user==a[i]:
            count=count+1
        i=i+1
    print(count)
count()
