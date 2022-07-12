# default_argument
# def sum(a=5,b=7):
#     print(a+b)
# sum(a=3,b=5)




# #######Possition###########
# def sum(a,b):
#     c=a+b
#     print(c)
# sum(4,5)

# #########keyword_argument#########
# def sum(a,b):
#     print(a+b)
# sum(b="archana",a="12")


# def my_function(child3, child2, child1):
#       print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


########### arbitary_argument###########
# def my_function(**kid):
#       print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")


############ arbitrary_key_argu#########
def d(*name):
    print(name)
d(5,6)