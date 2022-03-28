time=int(input("enter the car take time:-"))
i=0
while i<time:
    bike=int(input("enter the time of bike:-"))
    car=int(input("enter the time of car:-"))
    if bike<car:
        print("BIKE")
    elif bike==car:
        print("SAME")
    else:
        print("CAR")
    i=i+1