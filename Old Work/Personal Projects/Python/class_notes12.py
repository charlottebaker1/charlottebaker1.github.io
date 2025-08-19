#CLASS NOTES - tuples

#question:
a = 101
if a >= 0 and a <= 100:
    print("Great Job!")
#what woul dbe siplayed in the print statement if anything?
#nothing would be displayed as a was assigned 101 and because of the 'and' statement it does not satisfy those conditions

#Tuples
# a tuple consists of a number value seperated by commas
#you will group these values together by surounding them with parentheses

#example:
year_born = ("Winston Churchill",1874)

#rules:
#tuples are identical to lists, except for the following:
#(1) tuples are defined by enclosing the elementsin parentheses instead of square brackets
#(2) a tuple is an immutable list (a tuple cannot be changed in any way once it has been created)

#how to access a tuple using the index:
t = ("tuples","are","immutable")
print(t[0])

t1 = (12345, 54321, "hello!")
print(t1[0])

#nested tuples:
#assign out first tuple
t2 = (t1,1,2,3,4,5)
print(t2)
print(t2[2])
#whenever you see a problem with a nested tuple -- write it out!!
#the nested tuple is considered one item for the index (not individual)
#but you can reference within another reference
print(t2[0][0])
#print result -- 12345
#the t1 tuple would be printed inside

#to create a singleton tuple:
a = (2,)
#need to include the comma and parentheses for a single item tuple^^^

tup = (50,60,70,80,90,(200,201))
print(tup[5])
#This would print 200,201


