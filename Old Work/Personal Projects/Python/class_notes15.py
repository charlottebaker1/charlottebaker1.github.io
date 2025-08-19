#Class Notes 4/13/22 + Quiz Six Review

list = ['buffalo','penguin',10.0,45,'matilda']
list_three = ['simple','programming is near']
list_four = ['mary',100,'evie']
list_five = list + list_three + list_four
print(list_five[4])
#will print -- matilda

tuple_one = (12345,'abcde','hello!')
list_two = [tuple_one,('Santa',45.0,'Movies')]
print(len(list_two))
#will print -- 2

n = 6
b = 4
move = n + b
while b > 0:
    b -= 1
    if b == 2:
        continue
    elif b >= 4:
        print("The value of move is {}.".format(move))
        break
    print(b)
print('loop ended')
#will print --
#3
#1
#0
#loop ended


count = 1
for i in 'Evelyn':
    print('Letter {} is the {} element printed.'.format(i,count))
    print(count)
#will print --
#(will go through each print statement for evelyn) with 1 for count
#1 (There is no count increment so it doesn't increase)

def count_a(text):
    count = 0
    for letter in text:
        if letter == 'a':
            count = count + 1
    return(count)

print(count_a('anteater'))
#will print --
#2

