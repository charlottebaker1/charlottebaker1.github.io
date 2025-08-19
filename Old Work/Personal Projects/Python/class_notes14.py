#Class Notes 4/11
#reviewing function and more notes

'''
#product calculator function
def product_calc(x,y):
    answer = x*y
    print(answer)

u_i = int(input('Please enter a number to be muliplied: '))
u_i2 = int(input('Please enter a number to be muliplied: '))

product_calc(u_i,u_i2)

#you can concatonate two strings together using the '+'
print('hello' + 'world')

#printing format statements
print('My name is {1}, {0} {1}'.format('James','Bond'))

#f string
age = 40
print(f'I am {age} years old')
print()

first = 'james'
last = 'bond'
age = 90
print(f'The name is {last}, {first} {last}')

#print statements and the named arguments that can be used
#print(*objects, sep = ' ', end = '\n',
#the objects argument in our print statement is accessible as a list inside the function

#use the print function to have 3 sentences on the same line using 3 seperate print statements
def sentences():
    print('The first sentence', end='.')
    print('The second sentence', end='.')
    print('The last sentence.')

sentences()

#Let's say we want to use our end and seperation arguments
def planets():
    print('Mercury','Venus','Earth', sep= ',', end= ',')
    print('Mars','Jupiter','Saturn', sep= ',', end= ',')
    print('Neptune','Uranus', sep= ',')

planets()

#When we think about our print statements it comes with a default parameter called 'end,'
#in other words by defualt print() automatically adds '\n' to the end of each string before printing
#'\n' is a new line
#you can adjust the default value using sep = ' ' or end = ' '


import random
#create a list of animals , and after it is populated we will remove items randomly until
# there is only one item remaining in the list
animals = ['dog','cat','buffalo','bear','bee','rabbit']
while len(animals) > 1:
    #create a variable to hold randomly generated number
    eliminate = random.randint(0,len(animals)-1)
    del animals[eliminate]
print(animals)

#float example
#a float is a 50.0, 7.243
#casting to a float like you would an integer
weight = float(input('How many pounds is your suitcase: '))
if weight > 50:
    print('There is a $25.00 fee for your luggage.')

print('Thank you for your business!')

'''

#create a function to build a list of random numbers that are displayed to the user in a single list
#and that will also display the sum of the numbers in the list to the user
#they will be between 1 and 100
#the user will input how many numbers to include

total = 0

def sum2(x):

