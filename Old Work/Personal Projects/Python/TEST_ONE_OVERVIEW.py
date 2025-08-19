#CLASS 3/21/22
#TEST REVIEW
x = 4
x = y
y = y + 1
print(x)
#What would be printed? -- 4

pear = 4
grapes = 4.0
x = 'buffalo'
#What object type would be assigned to x? -- string data type

fruit_number = input('Pleas enter the number of fruits....:')
#Would this work to go through a function -- NO (didn't cast to an integer int())

import turtle
yertle = turtle.Turtle()
yertle.forward(65)
yertle.left(90)
yertle.setposition(0,0)
yertle.forward(100)
if yertle.distance(0,0) > 100:
    yertle.shape('turtle')
    yertle.penup()
    return_home()
    yertle.pendown()
    yertle.forward(50)
else:
    yertle.shape('arrow')
    yertle.forward(70)
yertle.forward(100)
#What shape will it be -- Arrow

myList = [5,9,17,3]
new_list = []
num = 0
while num < len(myList):
    num = num + 1
    new_list.append(num)
print(new_list)
#What will this print statment ^ display? -- [1,2,3,4]
#len is length so len is 4 integers long not the numbers inside
#starts at 0 + 1 = 1 + 1 = 2 + 1 = 3 + 1 = 4

if / else
#Which is the optional? -- else

increment operator is +=

'a' in #file opening
#What does this mode mean? -- append

LetterNum = 1
for letter in 'Magician':
    print('Letter {} is {}'.format(LetterNum,letter))
    LetterNum += 1
    if LetterNum >= 4:
        print(letter)
        break
#What will be printed at the conclusion of this loop? -- g
#FIRST LOOP -- M is 1 + 1 = 2
#SECOND LOOP -- A is 2 + 1 = 3
#THIRD LOOP -- G is 3 + 1 = 4
# --> goes to the if print(letter) 4 is g
#The loops iteration is only complete once it hits the result of the if statement

#class problem workthrough
#problem: please display how mnay times the letter 'a' appears in the string

def count_a(text):
    count = 0
    for letter in text:
        if letter == 'a':
            count += 1
    return(count)
#combine this function in a function call
print(count_a('banana'))

function_result = count_a('orange')
print(function_result)

#test function problem
#write a function called animal_factoids that has 2 parameters specified -- creating a list of X elements
#randomly generated elements 1 - 100, randomly generated number increase by K, both K and X specified by user
import random


def animal_factoids(x, k):
    list = []
    add_on = 0
    for i in range(x):
        add_on = random.randint(1, 100)
        list.append(add_on + k)
    print(list)


u_i_num = int(input('How many number elements in the list: '))
u_i_interval = int(input('What interval to increase by: '))

animal_factoids(u_i_num, u_i_interval)




