#Charlotte Baker
#CSCE101 005
#01/27/2022
#crb27@email.sc.edu
#Lab 02 - Input from the User and Mathematical Operations
#Celsius to Fahrenheit: (C x 9/5) + 32 = F
#Fahrenheit to Celsius: (F-32) x 5/9 = C
u_celsius=int(input("Please enter the temperature that you would like me to convert to fahrenheit: "))
celsius_to_fahren=(u_celsius*9/5)+32
print("The temperature {} degrees Celsius is {} degrees Fahrenheit.".format(u_celsius,celsius_to_fahren))

u_fahren=int(input("Please enter the temperature that you would like me to convert to celsius: "))
fahren_to_celsius=(u_fahren-32)*5/9
print("The temperature {} degrees Fahrenheit is {} degrees Celsius.".format(u_fahren,fahren_to_celsius))
print("Thank you for using the program! My name is Charlotte Baker.")
