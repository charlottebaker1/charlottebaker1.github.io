#Class Notes 1/31/22

#Start with functions

#Create the function signature - first line
#keyword def followed by the name of the function, followed by parentheses in which you will place the parameters
#parameters in general terms are the information that you need to give to the function so that it can work
#when you think about whether a function will need to have information specified in the parentheses
#as parameters, think about whether the function itself has everything it needs or whether it requires additional info
#This function will take a number and multiply it by 2
def doubler(num):
    num_doubled = num*2
    print(num_doubled)

#set up a problem where we need to get user's input for the number to multiply by 2
u_i = int(input("Please enter a number to be multiplied by 2: "))

#This is a function call
#function call - call the name of the function
#inside the parentheses is the argument that is passed to the function
#^ above num is serving as a placeholder for the information to be passed up and run through the function
doubler(u_i)

#create a new function that doesn't require anything to be passed to it, this it has no specified parameters
#all this function will do is print hello when its called
def sayHello():
    print("Hello!")

#because there are no parameters specified in the function parameters line, you know that you will not pass
#any information to the function call as arguments
sayHello()

#let's create a function with multiple parameters
#function signature line
def return_difference(num1,num2):
    print(num1-num2)

jars=15
cylinders=50
return_difference(cylinders,jars)

#create a function that will calculate two grades that are equally weighted, and the 2 grades will be recieved
#as input from the user
def grade_averager(grade1,grade2):
    #body of the function
    grade_average=(grade1*0.5)+(grade2*0.5)
    print(grade_average)


input_grade1=int(input("Please enter the first grade: "))
input_grade2=int(input("Please enter the second grade: "))
#call the function
#if you have a function with multiple parameters you will have a function call that specified multiple arguments to pass
#understand that the order you place your arguments in within the function call matters and will be the same order as
#the order of the parameters specified in the signature line
grade_averager(input_grade1,input_grade2)

#VARIABLE SCOPE AND LIFE: GLOBAL VS LOCAL VARIABLES
#a variable that is defined inside a function is local to that function
#where a variable is accessible and how long it exists depends on how it is defined
#we call the part of a program where the variable is accessible its - scope and the duration - the variable's lifetime

#a variable that is defined inside a function is local to that function
#a local function is accessible at the point it is defined until the end of the function
#and exists for as long as the function is executing
#the parameter names in the function definition behave like local variables but theu contain the values that we pass
#into the function when we call it

#by default, when we use the assignment operator inside of a function, the default is to create a new local variable
#unless a variable with the same name is already defined in the local scope

def grade_averager(grade1,grade2):
    #body of the function
    grade_average=(grade1*0.5)+(grade2*0.5)
    print(grade_average)
#The scope of this grade_average variable is LOCAL - cannot be used after in the program - only exists inside the
#body of this function

input_grade1=int(input("Please enter the first grade: "))
input_grade2=int(input("Please enter the second grade: "))
grade_averager(input_grade1,input_grade2)

#Let's do an example where we are going to assign a number to a variable before the function
#assignment statement
print_number=0
#create a function to print numbers
def printing_function():
    print_number=3
    print(print_number)

#call the function
printing_function()
print()
print(print_number)
#with this it is going to print 0 NOT 3 becuas 3 only exists as print number INSIDE the printing function
#the value assigned to print number NOW is outside the scope of the def function

def subtractor(numb1,numb2):
    equation=(numb1-numb2)
    print("The answer to the problem is {}.".format(equation))

input_numb1=int(input("Please enter the first number: "))
input_numb2=int(input("Please enter the second number: "))
subtractor(input_numb1,input_numb2)
