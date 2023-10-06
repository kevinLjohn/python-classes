
# PYTHON QUIZ # 2

# This is an open book test. You may use the internet to assist with your answers- NO PHONES ALLOWED!
# You will have the entire class time to complete your quiz. It must be submitted before class is over to recieve a grade.
# Take your time, read the questions thoroughly, find context clues and keywords to help you. 

# GOOD LUCK!
#-----------------------------------------------------------------------------------------------------------#

# 1. Create a function that will multiply two (2) values that are passed into the function as arguments. 
# Your function should print out the result of the two numbers that have been multiplied.
def multiply():
    num1 = 20
    num2 = 2
    print("Your two numbers that will be multiplied by 2 are 2 and 20")
    print(num1 *2)
    print(num2 *2)

multiply()
# 2. Creat a function that will do the following calculation. Your function should take in three argument. it should add the first
# two arguments and then the sum of the first two (2) should be divided by the third argument. 
# You function should then print the result. 

def triargument():
    print('argument1')
    a = input("type yes or no ")
    if a == 'yes'
        print("Third argument")
    else
        print("argument three")

triargument()
# 3. Create a elevator function that will run specific lines of code based on the conditions provided by a user. If the user types in 101,
# the function should print out they are going to the boys latin office, if they type in 203, they are going to the gym, 
# and if they type in the letter g, the lobby. else, if the input doesnt match any of the values provided, tell the user that floor doesn't exist and to please
# enter a valid floor number.

def roomnumber():
    c = input("put in either 203, 101 or g")
    if c = '203'
        print("go to the gym")
    elif c = '101'
        print('go to the office')
    elif c = 'g'
        print('go to the lobby')
    else
        print('floor does not esist')

roomnumber()
# hint you will need to look into using conditional statements

# 4. Write a simple conditional statement that uses a boolean that will print if it is daytime or nighttime.
day = input('is it daytime or night time')
print('it is ' + day)
# 5. What function would you use if you wanted to add and element/ value to a list data type? Explain why you would use it.

#You would use append because the main function of it is to add things to an list

# 6. Do some research and find the correct built-in python function that will reverse the order of the following list.
# then print your list in the reverse order.

random_number_list = [0,1,2,3,4,5,6,7,8]
random_number_list.reverse
# 7.Do some research and find the correcrt built-in python function that will allow you to find the largest number in the following list.
# then print the largest number
ranom_number_list2 = [100,230,40,39403,19]
max(ranom_number_list2)
# 8. A security company has hired you as an engineer to help them develop a program that will only let users into the building 
# if they enter a specific password. They given you the following information to use to build this program.
# - they want users to be able to enter a series of codes to get access
# - they want the user to enter an initial password value which is 0001
# - if they get this correct, they then want them to enter another value, which is 3039
# - if this is correct they will get access to the building
# - if they have the wrong answer in either scenario they will get a message saying access denied. 
def security():
    firstcode = input("put in the first password")
    if firstcode = '0001'
        print('correct')
    else
        print('wrong password')
    secondcode = input('now put in the second code ')
    if secondcode = '3039'
        print('access granted')
    else
        print('access denied')

security()
# 9. What does it mean to call a function? Why do we call functions. 
# you can use the variable below to enter you ansewer. 
answer9='to call a function means to activate it, we call functions to use them'

# 10. Find and print each value at the specific indexes provided in the list.
# find and print the values/words at index 3, 4, and 6 

shopping_cart = ['apples','water','chicken','ice cream','ground beef','string beans','oranges']
print(shopping_cart[3])
print(shopping_cart[4])
print(shopping_cart[6])