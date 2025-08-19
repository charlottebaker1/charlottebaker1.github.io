#Class notes for 1/24/22 + 1/26/22

#create a problem statement
#ask the user for the current temperature outside and if the user's input is 80 degrees or above we will
#tell the user the weather is hot that day, but if the temp is otherwise we will tell the user its nice outside
#we are going to assume that the user's input will be an integer

#Let's get user input
#Let's say we are going to cast this string input to an integer
current_temp=int(input("Please enter the current temperature in degrees outside:"))
#now, lets say we want to cast this string to a float
#current_temp=float(input("Please enter the current temperature in degrees outside:"))

#boolean operators
#== to show equality
#> greater than
    #this will pick up values from 81 and above
#>= greater than or equal to
    #this will pick up values (inclusive of) 80 and above
#< less than
#< less than or equal to

#syntax for an if statement:
#if <BOOLEAN EXPRESSION>:
#[tab] (make sure it goes over 5 spaces) <STATEMENT_1>
#else:
    #[tab] <STATEMENT_2>

#the syntax for an if statement
#our if statement will be evaluated first, and only if the if statement evaluates to true, will the statement indented below execute
#if current_temp>=80:print("It is hot outside!")
#else:print("The weather is nice outside!")


#if current_temp==0:
        #print("It is cold outside!")
#else:
    #print("You should check the weather!")
#print("Your weather check is complete!")
#above - an else statement is not always necessary - when using an if its built in. if the if isnt true it will skip to the nxt line and print^^
#if you keep the if statement and do indented statements below it - those will all be executed if the if is true (same thing with else)


#only one of these will be executed depending on the user input (if if isnt true, and elif isnt true, then the else will be executed as a "catch all"
#if current_temp>=80:
    #print("It is hot outside!")
#elif current_temp<=32:
    #print("It is cold outside!")
#else:
    #print("It is nice outside!")

#print("Finished")

#if you have two conditions, consider your if/elif/else

################################# NEW PROBLEM STATEMENT ######################################
#you are asked to average the grades input by a teacher. A class grade is comprised by 2 tests that are equally weighted
#if the resulting grade is greater than or equal to a 60, tell the user that the student recieved a passing grade
#if not tell the user that the student failed
#assume that the grades entered by the user will be integers

#ask the user for a grade for test one
test_one=int(input("Please provide the student's grade for test one: "))

test_two=int(input("Please provide the student's grade for test two: "))

#create a variable to store the product of these two grades each weighted 50%
weighted_average=(test_one*0.5)+(test_two*0.5)

#if weighted_average>=60:
    #print("The user recieved a passing grade!")
#else:
    #print("Unfortunately, the user failed the class.")

if weighted_average>=80:
    print("You did well!")
elif weighted_average<=40:
    print("Please try harder!")
else:
    print("Please try again!")

































