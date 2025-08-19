#CLASS NOTES 2/23/22 -- using files cont.

#example 2

#we know we need to open() a file for this problem
#for this problem -- we will take a text file, find the number of lines, we we also find the total sum of numbers in
#the text file, and you will need to display the minimum number in the file
#you can assume that the text file we are reading in only has numbers, no blank lines
#at the conclusion display the results (number of lines and total sum) to the user

#we will need to open the file and use a variable
#we will need to use our .readline() method

input_file = open('FILE NAME GOES HERE','r')

#we will need a line count variable; we will need a total sum variable
#we will need to cast the string input to integers to get our sum
#we will also need to store the minimum value we come across

#remember that the .readline() method returns an empty string once all the contents of a file have been read
#if you try to attempt to read with the readline after reading the entire file, you will always get the result
#of the empty string

#create a variable to hold each line read in the file
line = input_file.readline()

#create a variable to keep track of the line count
line_count = 0

#create a variable to store the minimum value we come across in the file
#we know the maximum value is 7845
minimum_value = 7846

#create a variable to store our total
total = 0

#why is line controlling our while loop?

#set up a while loop
while line:
    #we will need to increment our variable that is keeping track of the number of lines in the file
    line_count += 1
#we will need to store the current value that is being read in the file; we will also need to cast
#that input to an integer
    temp = int(line)
    total = total + temp
    #create a variable to hold the value we will be comparing to the minimum
    comp_value = int(line)