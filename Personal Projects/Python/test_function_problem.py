import random
def animal_factoids(x,k):
    list = []
    add_on = 0
    for i in range(x):
        add_on = random.randint(1,100)
        list.append(add_on + k)
    print(list)



u_i_num = int(input('How many number elements in the list: '))
u_i_interval = int(input('What interval to increase by: '))

animal_factoids(u_i_num,u_i_interval)