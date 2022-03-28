def neg():
    list1 = [2, -7, 5, -64, -14]
    i=0
    count_pos=0
    count_neg=0
    while i<len(list1):
        if list1[i]>0:
            count_pos=count_pos+1
        elif list1[i]<0:
            count_neg=count_neg+1
        i=i+1
    print("pos num",count_pos)
    print("neg num",count_neg)
neg()
