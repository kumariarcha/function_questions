def pahindrome(string):
    string_list=list(string)
    i=-1
    a=[]
    while i>=-len(string):
        a.append(string[i])
        i=i-1
    if string_list==a:
        print(string,"is pahindrome")
    else:
        print(string,"is not pahindrome")
string=input("enter the string")
pahindrome(string)
