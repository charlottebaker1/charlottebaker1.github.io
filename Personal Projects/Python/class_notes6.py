#Class Notes 2/7/22

#While loop
#a while loop is an event controlled loop statement and you use a while loop when you do not know how many times you will
#have to execute the body of a loop beforehand

#a while loop will continue to repeat as long as the condition is true
#3 important parts: initialization, condition, and the update
#in the initialization step, you set up the variable which you will use as the condition
#in the condition step you perform a test on the variable to see whether you should terminate or execute
#then after each successfully completed execution of the loop body, you will update your variable
#**Note: that the condition is checked before the loop body is executed for the first time
#** if the condition is false at the start the loop body will never be executed

#increment operator +=
#decrement operator -=
#what the increment operator means is as follows:
#number = 10
#number += 1
#number = number+1

#total - initialization
#total=0
#i=1

#while i < 10:
   # total += i
    #i += 1
   # print(total)

#increment before printing the total

#our first step at the condition - we will initialize our value of i to 1
#next, you will check whether i is less than 10, and if this is true you will update i
#by incrementing it by 1
#we will keep a running total that will be assigned temporarily each iteration of the loop to the variable total


#EXAMPLE 2 -- WE WILL JUST HAVE THE TOTAL DISPLAYED UPON THE CONCLUSION OF THE WHILE LOOP
#total - initialization
total=0
i=1

while i < 10:
    total += i
    i += 1
print(total)
#if print is in - whole list displayed
#if print is out - only the end total
#ALWAYS make sure you are incrementing inside the body of the loop
#caution: a while loop can create what's called an infinite loop if the halting condition is never met
#if it doesnt evaluate to false

#lists
#a list is a data structure that can hold an ordered collection of items
#you create a list similar to how you create a variable; whatever elements you would like to include in the list
#put in brackets
#example
animals = ['dog','cat','horse','kangaroo']

#let's say we want to print the 2nd element in the animals list
print(animals[1])
#it starts counting at ZERO so the #1 element is really the second and the #0 element is the first
print(animals[2])
print(animals[-1])

#in order to use the random module we will import random
#you should import random at the beginning of your script
import random

#create an empty list
numbers = []

#problem statement: Let's say we want to print a list with contents in the range of numbers
#1 to 10 and then print it
#range(start, stop, increment)
#if we only have one number specififed in the parameters that is by default the stopping condition
#we can also specify where we want our range to begin and in what increments we want the contents to increase/decrease
#by default the starting condition of range is 0, so if you have two values in your range parameters, you will have
#specified the starting ans stopping conditions
for i in range(1,10):
    #append an element to our numbers list using the .append() method
    numbers.append(i)
print(numbers)
#your stopping condition for range will always be n-1
#because in this 10 isn't between 1 and 10 it will not work (change to 11 - 10 will be included)
#below - this will also work to include the 10
numbers2=[]
for i in range(10):
    #append an element to our numbers list using the .append() method
    numbers2.append(i+1)
print(numbers2)

#Let's say that we are asking the user to input elements of a list comprised by the name of 8 animals
#step 1: create a list
animals2=[]
#len=len will evaluate the number of items in a list
while len(animals2)<=3:
    temp = input("Please provide an animal type: ")
    #use .append() to add the animals input by the user to the animals2 list
    animals2.append(temp)
    #temp will store what the user will store as an animal type each time the loop iterates, which will then be appended
print(animals2)
#starts counting at 0









