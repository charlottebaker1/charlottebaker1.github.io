#CLASS NOTES

#problem statement: create a function with one parameter that will count the number
#of times that a letter appears in a word that the user inputs

#len function - when applied to a string it will return the number of characters in a string
#same notion of an index that starts counting at 0
#so if you're referencing the character in a string still 1st is 0

def count_letters(word):
    x = len(word)
    print(x)


#need user input
u_a_word = str(input('Please enter the word of your choice: '))
#casting it to a string just to show it is a string and will be interpreted as such
#call the function
count_letters(u_a_word)

#create an empty list
friends = []
friends_close = ['Joe','Brad','Denise','Beau']
for friend in friends_close:
    print(friend)

#concatonate with a string
for fruit in ['banana','kiwi','mango','orange']:
    print('I like to eat '+ fruit + 's!')

#len with a string
greeting = 'Good Day'
print(len(greeting))

#len with a tuple example
london_coordinates = (51.50722,-0.1275)
print(len(london_coordinates))

#The len function will always print an integer since it is counting the number of items in the object
#passed to it

#BREAK VERSUS CONTINUE STATEMENT
#break statement immediately terminates a loop while the continue statement terminates
#the current loop iteration (each time the loop is run so that specific run)
#in a continue statement, execution will jump to the top of the loop and to the controlling expression
#which will be re-evealuated to determine whether the loop will execute again

#break statement example
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('loop ended')
#output:
#4
#3
#loop ended

#continue statement example
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
        #when n == 2 the continue statement causes the termination of that iteration of the loop
        #thus, print(n) when n == 2 is not printed instead the interpreter returns to the top of the loop
        #the condition is reevaluated and it is still true when n == 2 2>0 the loop resumes
    print(n)
print('loop ended')
#output:
#4
#3
#1
#0
#loop ended

#RETURN STATEMENT
#the python return statement is a key component of functions and methods
#you can use this to make your functions send python codes back to the caller code
#these objects that are returned are known as the functions return value
#in general, a function takes arguments (if any) performs some operations, and returns a value
#(or an object)
#this return onject or value is the functions return value
#pythons return statement is a special statement that you can use inside a function or method to send
#the functions result back to the user or to whatever function called the function
#and it can be used to perform further computations in your programs
#syntax: a return statement consists of the return keyword followed by the optional return value

#an explicit return statement immediately terminated a function execution and sends the return value back to the caller
def square(num):
    num_squared = num ** 2
    #double multiplication operator is exponent (in this case squaring it)
    return num_squared

#we need input to pass to the function as an argument to take the place of 'num'
input_num = 5
output_num = square(input_num)
print(output_num)

#problem statement: let's say you want to ask the user to input items until a list is populated with
#elements of a certain number
ice_cream = ['peach','sorbet']
while len(ice_cream) < 6:
    temp = input('Please enter an ice cream flavor: ')
    ice_cream.append(temp)

print(ice_cream)
print(len(ice_cream))
#['peach','sorbet','blue','red','green']
#    1       2       3      4     5  - element numbers! (what len will produce)
#    0       1       2      3     4  - index numbers! (only when referencing a specific element with index)


#BOOLEAN COMPARISON VALUE -- truth tables
#3 comparison operators: and, not, or
#string example using chained conditionals joined by boolean comparison operators
food = input('What is your favorite food: ')
drink = input('What is your favorite drink: ')

if food == 'pizza' and drink == 'juice':
    print('Those are my favorites as well')
else:
    print('One of those is not my favorite')
#asking for user input -- DO NOT a = print(input('Please ask for ....
#DO NOT: b = print('What is your fav ...







