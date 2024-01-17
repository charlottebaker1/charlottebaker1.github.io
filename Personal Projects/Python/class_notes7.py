#Class Notes 2/9/22


#problem statement: use a function to create a list and fill it while also adding  the number elements
#to a list specified by the user and displaying the results to the user

#need a function -- need a function signature line
#ask for users input outside of the function -- one parameter
#how do we know the function will have one parameter?
def populate_and_print(x):
    numbers_list = []
    for i in range(1,x+1):
        #.append()
        numbers_list.append(i)
    print(numbers_list)


u_i = int(input("Please enter the number of items in a list you would like to include: "))

populate_and_print(u_i)

#new problem statement: you are asked to create a list of numbers with x elements that increment by K
#where x and k values are recieved from the user
#ask the user for how many number elements they would like to include in the list and to specify the interval they
#would like the numbers to increase by then display the results to the user

#signature line
def create_list_with_increments(x,k):
    temp_list = []
    increment = 1
    #loop - we will use a for loop because we know how many times the loop with iterate (i.e. the user's x input)
    for i in range(1,x+1):
        increment += k #this means that python adds another variables value here which is k
        #and then assigns the incremented value to the variable increment
        temp_list.append(increment)
    print(temp_list)

u_i_x = int(input("Please enter the number of items in a list you would like to include: "))
u_i_k = int(input("Please enter the increment by which you would like each number in the list to increase by: "))

create_list_with_increments(u_i_x,u_i_k)




