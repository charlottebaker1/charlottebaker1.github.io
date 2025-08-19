#Class Notes 2/14

#problem statement: say you want to read items from the user until your list is a certain size,
#and then we will remove items from the list
#and then display the list to the user
import random

animal = ['monkey','cat','horse','cheetah','dog','buffalo','zebra','lion']

animal2 = []

#create a while loop that we will use to populate our second list using user's input
while len(animal2)<=8:
    temp = input("Please enter an animal: ")
    #the len is going to count the number of items in the list
    #we will need to append each animal input by the user to our list
    animal2.append(temp)
    print(animal2)
#if the print is inside, it prints every time one is entered
#outside - it prints the final list after every input is entered

#problem statement: Let's modify the program above in order to have a random element removed from our list until
#only one element remains
animal = []
while len(animal)>1:
    eliminate = random.randint(0,len(animal)-1)
    del animal[eliminate]
    print(animal)
