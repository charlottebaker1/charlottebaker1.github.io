#CLASS NOTES 2/21 - using files (opening,closing, writing, reading)

#file input and output

#Let's say that you want to open a file - this is done by invoking the built in function
#.open(), which ahs a single required argument that is the path to the file or if stored in the same
# place as your programming file, it is the file name in quotes
#once the arguments are specified .open() will return a file object
#and will operate within one of three modes:
# (1) read - 'r' - reading a file
# (2) write - 'w' - writing to a new file
# (3) append - 'a' - adding to the end of a file
#by default it will be read

#this is saying open the file and read its contents
file_cb = open('FILE NAME HERE','r')

#to print the entire contents - create a variable to display the contents
file_data = file_cb.read()

#if we want to display the contents of this file to my display console
print(file_data)

#anytime you open a file - make sure you close it when youre done
# if you dont it could create problems in and outside of your program

file_cb.close()

#if we want to write the contents of the file in file_cb to a new file
file_cb = open('FILE NAME HERE','r')

#w -- means we are opening the file for writing or truncating (overwriting)
#if there is no file with the specified name it will be created
file_new = open('FILE TO WRITE TO HERE','w')

#let's say we want to through the contents of an prigingal file and add line numbers to a new file
#that has the same contents as the original file
#start with a while loop
#create a variable to keep track of the number of lines in our file
line_num = 1

while True:
    #we will use a .readline() method that will read each line in the file one by one
    #when we return an empty string, the while condition of True will be False and the loop will stop
    line = file_cb.readline()
    #here we are assigning each line to the variable line
    #we are placing the first variable assignment to line of the .readline() method within the body of the while loop
    #also, we will need to think about the structure of the file we are reading, and whether just an empty string will work
    #Check your text file before you start
    if len(line) == 0:
        break
    #Let's say you want to add line numbers to each line in a file as long as the length is greater than zero
    file_new.write(str(line_num)+' :'+line)
    line_num += 1

file_new.close()
file_cb.close()

