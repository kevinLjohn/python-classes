# MID TERM QUIZ 


# RULES

# I. You may use google/ W3 schools to assist you with this exam

# II. You may use notes in your reposiory

# III. You may not use any additional computing devices 
# (only one computer should be out).

# IV. You may not use your phone during the quiz under any circumstances.
# If it is an emergency please request to be excused from the class. 

# V. You may not have music or videos playing during the quiz
# under any circumstances. 

# VI. You may not use any LLM / AI applications under any circumstances. 
# Any one caught using  these applications will automatically fail the quiz.

# _____________________________________________________________________


# Take your time, read the questions thoroughly, look for context clues

# GOOD LUCK

# _____________________________________________________________________



# 1. Describe what a computer program is and what does it do. 
 
#a computer program is prebuilt code that allows the omputer to function

# 2. Describe what complexitity and abstraction are, then provide an example
# of complexity in the real world and how we apply abstraction to that thing (you example must be original and cannot be an example
# used in our lecture slides ie car, grocery store, etc.). 
  
#abstraction hides unneeded code. complexitity counts the number of operations 

# 3. What is Syntax in Python and why is it important to write proper syntax?

#Syntax is the rules that define python and it's important because it's what makes python work.

# 4. What is a function, and why do we wrap our code inside of functions?

#A function is a conatiner of code that we create using the def verible. We wrap our code inside of functions
#to make our code more organized 

# 5. Name and describe the three (3) naming conventions for variables in python? Then provide three (3) name rules for Python
# variables. 

#rule 1: it's can't start with a number rule 2: it can't have a space in it, rule 3: No symbols other than _


# 6. What will be the output of the print functons when this code is ran, explain why
name = 'Bill'
student = name
name = 'Walter'
student= 'Richard'

print(name)
print(student)

#It will print Walter and Richard because at the end they change what's inside of both veribles.

# 7. Describe the difference between each of the following assignment operators:
# = number wise
# == to tell a while command if two statements are the same
# != if something isn't equal to
 
# 8. What type of data can be stored in a python list?

#Strings, int, float, and veribles

# 9. Create a function that will take in a word provided by a user and then output that word back to the user but in reverse. 

word = input("type a word now! ")

def reversedword():
    drow = word[::-1]
    print(drow)

reversedword()

# 10. Create three (3) seperate functions that will do addition, subtraction, and multiplication respectively. 
# each of these functions should take two (2) arguments. When the user passes these arguments into the function, they will be
# calculated together and return the output in your terminal. 

def math():
    add = input("type a number ")
    print(add + 3)
    print(add*3)
    print(add - 3)

math()

# 11. What is the difference between a function argument and a function parameter. 

# a parameter is a placeholder and the argument is the code itself

# 12. You have been hired by a software company and your first assignment is to develop a password authenticator program. 
# the goal of your program is to check a user's password and make sure it meets the company's password requirements. 
# the company has provided you with the following requirements for the passcode program:
# a. the passcode must NOT contain any numbers
# b. the passcode must NOT contain any capital letters
# c. the passcode can NOT be any longer than five (5) characters
# d. the passcode can NOT shorter the three (3) characters
# e. the user should be able to enter their password and if it meets the requirements, should print a message saying that 
# their password was created successfully, and if it was not, should send back a message with one of the following issues. 

def password():
    passw = input("Enter the password you want ")
    print("Your new password is " + passw)

password()

# 13. When you run your code and see typeError in your terminal, what does that typically mean and how would you try to solve
# the issue?

#it means you are using the wrong data type in your code and you cn fix it by using str or int where needed

# 14. When you run your code and see indentError in your terminal, what does that typically mean and how would you try to solve 
# the issue?

#it means you are using the wrong type of function in your code

# 15. Create a while loop that check a user's password. If they enter the password correct, they will get a message saying 
# that the password was entered successfully. If they enter the password incorrectly, it will tell the user to try again. 
# The user should only have three (3) attempts to get the password correct. If they enter the password incorrect on the fourth 
# attempt, a message should appear telling them that have been locked out and need to talk to the administrator. 

passwordtwo = input("put in your passwrod ")

#while passwordtwo == "jakerocks"
#    print("You have logged in")
#else
#    print("You have been locked out your account for 27 years, call apple support for help")
#break

# 16. Which item is at index 5
giftShopping=['xbox','sneakers','necklace','clothing','laptop','gift card']

 #the index 5 item is the gift card

# 17. Create a for loop that will print ONLY the even numbers within the range of the variable provided below.
# HINT: You will need to use the range() function. 
upToNumber = 30
tw = 2
for tw in upToNumber
    print(upToNumber.range)

# 18. Create a function that uses a conditional statement that checks if a person qualifies for a raise on their salary. 
# The user should be able to enter their name, their salary (how much money they make in an entire year), and how long they have
# worked at the company. If the user has been working at the company longer than four (4) years, they will get a 15% raise. 
# Your program should be able to calculate what their salary is with the 15% increase. If the user qualifies, your program
# should return the a message congratulating the user by name, and telling them what their new salary is with the 15%
# increase (this must be the actual number). If they do not qualify inform the user that unfortunately they do not qualify. 

def raisem():
    req = input("do you work harder than everyone else? ")
    if req = 'yes'
        print('you can have raise')
    else:
        print('no')

raisem()

# 19. Create a function that checks which value is greater than the other. Your function should take two (2) integer parameters. 
# and should evaluate which number is larger. Your function should then print the largest number. 

def num5():
    num1 = input('type a number')
    num2 = input('type a second number')
    num3 = int(num1)
    num4 = int(num2)
    if num3 > num4:
        print(num1 + ' is greater than ' + num2)
    elif num4 > num3:
        print(num2 + ' is greater than ' + num1)
              
num5()


# 20. Create a while loop function that will add gift items to a list. Your function should ask the user to enter an item name. 
# The item name should then be added to a list variable called gift_bag. Your gift bag should have a limit of six (6) items. 
# Once your gift bag hits its limit of six (6) items your program should print a message saying 
# that the gift bag is full and print the list of items in the gift bag.   
 
li = ['book','ball','pan','cup','pot',]

add2 = input('add another item ')

add2.append(li)

print(li)