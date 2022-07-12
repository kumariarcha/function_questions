def more():
    expend=int(input("enter the number:-"))
    number=int(input("enter the number of student:-"))
    total=expend*number
    if total>=50000:
        print("your expenditure is",total)
    else:
        print("It is under budget")
more()