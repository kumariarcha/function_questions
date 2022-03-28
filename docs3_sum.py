from syslog import LOG_LOCAL2


def sum():
    list=[8,2,3,0,7]
    i=0
    sum=0
    while i<len(list):
        sum=sum+list[i]
        i=i+1
    print(sum)
sum()
