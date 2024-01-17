#Charlotte Baker
#CSCE 101- Lab 005
#2/13/2022
#crb27@email.sc.edu
#Lab 05 - Fun with Lists

def create_list_1(x):
    numbers_list = []
    for i in range(1,x+1):
        numbers_list.append(i)
    print(numbers_list)

u_i = int(input("Please enter the number of items in a list you would like to include: "))
create_list_1(u_i)

def create_list_2(x):
    temp_list = [0]
    increment = 0
    for i in range(0,x-1):
        increment += 5
        temp_list.append(increment)
    print(temp_list)

u_i_x = int(input("Please enter the number of items in a list you would like to include: "))
create_list_2(u_i_x)


def create_list_3(x):
    numbers = list(range(1,x+1))
    print(numbers)
    while len(numbers) > 1:
        del numbers[-1]
        print(numbers)

u_i3 = int(input("Please enter the number of items you would like to include in the list: "))
create_list_3(u_i3)

print("Thank you for using the program! My name is Charlotte Baker.")

