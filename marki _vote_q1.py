def vote():
    age=int(input("enter the age"))
    i=0
    while i<age:
        if age<18:
            print("you are not egibail")
            break
        else:
            print("you are egibail")
            break
    i=i+1
vote()