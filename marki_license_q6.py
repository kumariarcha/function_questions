def drive_licnese(speed):
    if speed<70:
        print("70")
    elif speed>70:
        i=71
        j=1
        while i<speed:
            if i%5==0:
                j=j+1
            i=i+1
        if j>12:
            print("license suspended")
        else:
            print(j)
drive_licnese(85)
drive_licnese(135)