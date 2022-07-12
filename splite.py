
# from more_exercise_q7 import string


def split():
    string = "my name is archana"
    i=0
    list=[]
    str2=" "
    while i<len(string):
        if string[i]==" ":
            list.append(str2)
            str2=""
            i=i+1
            continue
        else:
            str2=str2+string[i]
        i=i+1
    list.append(str2)
    print(list)
split()


 

