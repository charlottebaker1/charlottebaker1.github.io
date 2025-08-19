#2/28 Test Review + Practice Problems

#PROBLEM 1
#lists with indexes
a = [5,6,7,8,9,10]
print(a[4])
#what will this print?
#computer starts counting at zero
answer = 9


#PROBLEM 2
n = 100
if n >= 50:
    turtle.forward(100)
else:
    turtle.forward(0)
#In this case the turtle would not move forward

#PROBLEM 3
bananas = 0
def banana_tabualtor():
    bananas_count = 3
    print(bananas_count)
banana_tabulator()
print(bananas)
#This would print 3, then 0

#PROBLEM 4
import turtle
alex = turtle.Turtle()
alex.color('blue')
alex.pendown()
list_one = [1,2,3,4,5]
for i in list_one:
    alex.forward(i*i)
#When the loop goes through
#the first time i*i i=1 so 1x1 = 1
#second its 2x2=4, then 3x3=9, 4x4=16, 5x5=25 1+4+9+16+25 (alex will move all these steps as it goes through the loop)
#alex will move 55 units total


#PROBLEM 5
numbers = [5,6,32,21,9]
running_total = 0
for number in numbers:
    running_total = running_total + number
print(running_total)
#'number' in the for loop is a placeholder for the list elements
#it starts with the 5, adds the 'number' + running_total which is 0 at the start
#then running_total becomes 5 then the for loop runs through adding each list element
#and changing the value of 'running_total' each time
#it is then printed at the end outside the loop so it will only print one number

#PROBLEM 6
import random
random_value = random.randint(1,11)
#random.randint is inclusive
#so it could be 1,2,3,4,5,6,7,8,9,10,11
#IN THIS CASE - this isnt always true for other things but it is for random.randint

#PROBLEM 7
#quiz 2 - question 1
#it is asking us to create a function to ask the user for input for the number of integer elements
#to include in a list as well as the amount by which each item in the list will increase
#the function create_list_wSpecificElmentNos() should have 2 parameters and should display the
#final list created with the user's input to the user (make sure to call the function)
def create_list_wSpecificElmentNos(number,increment):
    increment_y = 1
    #create an empty list
    temp_list = []
    for i in range(number):
        increment_y += increment
        temp_list.append(increment)
    print(temp_list)



u_i_list_number = int(input('Please enter the number of items you would like to include in a list: '))
u_i_list_increment = int(input('Please enter the amount by which you would like the numbers to increase: '))

create_list_wSpecificElmentNos(u_i_list_number,u_i_list_increment)

