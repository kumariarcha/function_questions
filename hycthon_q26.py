# def ConvertHours(n):  
#     minutes = n * 60;
#     seconds = n * 3600;
#     print("Minutes = ", minutes \
#          ,", Seconds = " , seconds);
# n = 5;
# ConvertHours(n);
 
 
total_sum = 0
for i in range(1000):
    if (i%3 == 0 or i%5 == 0):
        total_sum = total_sum+i
print (total_sum)
