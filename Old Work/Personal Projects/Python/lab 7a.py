#Charlotte Baker
#CSCE 101 - Lab 005
#3/10/22
#crb27@email.sc.edu
#Lab 07A - Reading from a File

input_file = open('lab07_python.txt','r')
count = 0
total = 0
line_count = 0
line = input_file.readline()
min_value = 7845
max_value = 0
while line:
    line_count += 1
    temp = int(line)
    total = total + temp
    line = input_file.readline()
    if temp < min_value:
        min_value = temp
    if temp > max_value:
        max_value = temp
    avg = total/line_count


print('The total value is {}, the minimum value is {}, the maximum value is {}, and the average is {}'.format(total,min_value,max_value,avg))

print('Thank you for using the program! My name is Charlotte Baker')

