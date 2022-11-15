#Video: Starting Out With Python with ML 01

#Scalar Variables
x = 5
numStudents = 30
y = 3.0
z = "hello"
w = False
n = None

#Collections
#List
#listOfValues = [1, 2, 3, 4]
#x = listOfValues[0]

#Dictionary
dictOfValues = {
    '1a' : "Blue Honda Civic",
    '2c' : "Red Toyota Highlander"
}
z = dictOfValues['1a']

#Operations
#print("My variables: ", x, y, z, numStudents, n)
#print(listOfValues)

x = x+2

#print('X is now: ', x)

#Arithmetic
#+ - * / // % **

# print(10/3)
# print(10//3)
# print(10%3)
# print(10**3)

# #Comparison
# #> < >= <= == !=
# print(x==3)
# print(x<3)
# print('emu' < 'dog')

# #Logical
# #and or not
# print('False or False', False or False)
# # or -> true if either operand is
# print('True and True', True and True)
# #and -> true if both operands are true
# print(w and True)
# print((x < 3) or (y < 1000))
# print((x < 3) or (y < 1000) and x==7 or x == 92)

# if i >= 10:
#     print('Big number')
# elif i>=5:
#     print('Medium number')
# elif i>=1:
#     print("Smallish")
# else:
#     print('Small number'

#Looping
# secretNumber = 13
# i = int(input())
# while(i != secretNumber):
#     print('Wrong!')
#     i = int(input())
# print('Congratulations!')

for j in range(5, 10, 2):
    print('j is now: ', j)



exit()
