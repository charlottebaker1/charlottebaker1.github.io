#Charlotte Baker
#CSCE 101 Lab-005
#2/4/22
#crb27@email.sc.edu
#Lab 4 Part A - Functions

import random

def C_to_F(num1):
    equation=((num1*9/5)+32)
    print("This temperature in fahrenheit is: {}.".format(equation))

def F_to_C(num2):
    equation=((num2-32)*5/9)
    print("This temperature in celsius is: {}.".format(equation))

def generate_random_number (X):
    if X <= 0 or X > 50:
        raise ValueError("Count should not be negative or zero or greater than 50.")
    else:
        for i in range(X):
            print(random.randrange(1,100))

count = int(input("Enter the count of random numbers you want to generate: "))
generate_random_number(count)

input_celsius=int(input("Please enter the temperaure you would like me to convert to fahrenheit: "))
C_to_F(input_celsius)

input_fahren=int(input("Please enter the temoperature you would like me to convert to celsius: "))
F_to_C(input_fahren)

print("Thank you for using the program! My name is Charlotte Baker.")





