#1
#w= 300 is int
#x= “My name is Bill.” is print
#y= 12.34 is float
#z= True is bool

#2: no @myclass isn't a veriable because it has no function

#3: We do print(a+b+c)

#4: input allows the user to input a command to trigger something, print types out what we want written down, int coonverts a number to a integer, bool turns a veriable to true or false, and float turns a number to a floating point number

#5: 
age = int(input('how old are you: '))
if age > 17:
    print('you can buy this game')
else:
    print("YOU CAN'T BUY THIS GAME")
#6: 
height = float(input('how tall are you?: '))

if height > 5.5:
    print('you can go on this ride')
else:
    print("you're not allowed to ride this ride")


#7:

a_list:['milk','bread','juice','cookies','paint','tools','apples']

#8: 
def myfunction(name, age):
    if age > 18:
        print('hi ' + name)
        print('are you on your way to collage?')
    else:
        print("hi " + name)
        print('are you still in highschool?')
yourname= int(input('what is your name?: '))
yourage= int(input('how old are you?: '))
myfunction(yourname, yourage)