def number():
    num=int(input("enter the num"))
    i=1
    while i<=num:
        print("table of",i)
        j=1
        while j<=num:
            print(i,"*",j,"=",i*j)
            j=j+1
            print()
            i=i+1
number()


