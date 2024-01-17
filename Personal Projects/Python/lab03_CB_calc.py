#Charlotte Baker
#CSCE 101 Lab 005
#1/28/22
#crb27@email.sc.edu
#Lab 3 - Grade Calculator

test_one=int(input("Please provide the student's grade for test one: "))
test_two=int(input("Please provide the student's grade for test two: "))
lab_avg=int(input("Please provide the student's grade for the labs: "))
project=int(input("Plese provide the student's grade for the project: "))
quiz=int(input("Please provide the student's grade for the quiz: "))
weighted_average=(test_one*0.15)+(test_two*0.15)+(lab_avg*0.45)+(project*0.1)+(quiz*0.15)
if weighted_average>=90:
    print ("Your final grade is an A.")
    print ("Congratulations! Your grade is {}.".format(weighted_average))
elif weighted_average>=80:
    print("Your final grade is a B.")
    print ("Congratulations! Your grade is {}.".format(weighted_average))
elif weighted_average>=70:
    print("Your final grade is a C.")
    print ("Congratulations! Your grade is {}.".format(weighted_average))
elif weighted_average>=60:
    print("Your final grade is a D.")
    print ("Congratulations! Your grade is {}.".format(weighted_average))
else:
    print("Your final grade is an F.")
    print("Sorry! Your grade is {}.".format(weighted_average))
print("Thank you for using the program! My name is Charlotte Baker.")
