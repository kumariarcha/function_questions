
# def greet(names):
#     i=0
#     while i<len(names):
#         i=i+1
#     print("Welcome", names)
# greet("Rinki")



# def info(name, age  ):
#        print(name + " is " + age + " years old")
# info("Sana", "17")
# info("Umesh", "18")



# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)
# studentDetails("archana","funcation","devika")


# def function_print(name):
#     print("my name is",name)
#     print("I am the co-founder of NavGurukul.")
# function_print("rishabh")


def check_speed(speed):
    if speed <= 70:
        return 'Ok'
    elif speed >= 70:
        points = (speed - 70) // 5
        print('points = {}'.format(points))
        if points >= 12:
            return 'License suspended'
check_speed(80)
points = 2