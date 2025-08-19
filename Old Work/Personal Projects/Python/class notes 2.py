#Class Notes 1/19/22

#assign my name to a variable
f_name= "Charlotte"
age= "18"

#review of printing .format() method
print("My name is {}. I am {} years old.".format(f_name,age))
#formatting method is going to take the argument inside the parentheses of .format

#problem statement: let's have a number of shoes assigned to a variable and then multiply by three
#then display the results of the product to the user

shoe_number= 76
shoe_product= shoe_number* 3
#* is multiplication operatot
#calling the variable shoe_number when we multiply by 3 to get the product.
print(shoe_product)
#division operator is the /
#+ is addition
#- is subtraction

#modify our problem statement
#this time asking user for input on how many shoes they own
#then we will divide by 2
#then siplay the results by 2

#to get input from the user - using input prompt
#input() - this is the input prompt
#u_i=input()
#u_i=input("Please enter the number of shoes you own:")
#shoe_amount=u_i/2
#print statment will tell us what will be displayed to the user
#Print(shoe_amount)

#what data type do we need to perform arithemtic operations? integers, floats data types
#we will cast the input from the user which will always be a string data type by default into an integer
u_i=int(input("Please enter the number of shoes you own:"))
shoe_amount=u_i/2
print(shoe_amount)
#can use this template for various formulas

#let's say that we want to take the user's input for the number of apples they want from the store
#let's say that we need to multiply that input for apples by 2
#we also need to ask the user for the number of grapes they would like from the store
#then we need to combine the number of grapes with the nuber of apples and display the results to the user

#what we need to do

#we need to ask the user for input that we will store in our apples variable and do the same for graped
#next multiply apples input by 2
#then we need to combine the product of apples with the number of grapes (addition)
#finally, we need to display the result to the user using a print format statement

u_apples=int(input("Please enter the number of apples:"))
u_grapes=int(input("Please enter the number of grapes you would like from the store:"))
apples_amount=u_apples*2
#create a variable to store the total fruit amount
all_fruit=apples_amount+u_grapes
print("The total amount of fruit you have requested is {}.".format(all_fruit))


#fahrenheit to celsius formula: (F-32) x 5/9 = C
#ask the user for input of the degrees of fahrenheit that the user would then like to convert to celsius
#then you will display the converted result to the user
#assume the user will enter an integer (a whole numvber; natural number)
#since we will be converting the fahrenheit to celsius we will need to cast the input which will be a string - to an integer!!
u_fahrenheit=int(input("Please enter a temperature that you would like me to convert to celsius for your upcoming trip:"))
#add your parentheses because we will use PEMDAS - order of op - which is how interpreter reads interprets and computs formulas
fahren_to_celsius=(u_fahrenheit-32)*5/9
print(fahren_to_celsius)


























