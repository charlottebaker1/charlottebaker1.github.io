#Charlotte Baker
#CSCE 101 - Lab 005
#3/10/22#Charlotte Baker
#CSCE 101 - Lab 005
#3/10/22
#crb27@email.sc.edu
#Lab 08A - Reading and Writing to Files

input_file = open('lab08_python.txt','r')
file_data = input_file.read()
input_new = open('newfile','w')
line_num = 1

while True:
    line = input_file.readline()
    if len(line) == 0:
        break
    input_new.write(str(line_num)+' :'+line)
    line_num += 1

input_new.write(str('Charlotte Baker,005,'+(line_num)))
print('Thank you for using the program! My name is Charlotte Baker.')
#crb27@email.sc.edu
#Lab 08A - Reading and Writing to Files

input_file = open('lab08_python.txt','r')
file_data = input_file.read()
input_new = open('newfile','w')
line_num = 1

while True:
    line = input_file.readline()
    if len(line) == 0:
        break
    input_new.write(str(line_num)+' :'+line)
    line_num += 1

input_new.write(str('Charlotte Baker,005,'+(line_num)))
print('Thank you for using the program! My name is Charlotte Baker.')

