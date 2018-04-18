# This program asks for your name and says hello
# Written on 06/27/17

import random
import math

print('Hello World')
print('What is your name ?')
myname = ''
while len(myname) == 0  :
    print('Please type your name')
    myname = input()
    print(myname)
print('Hello ' + myname)
print('The length of your name is ' + str(len(myname)))
print('What is your age ?')
myage = str.strip(input())
while (str.isnumeric(str(myage))==False):
    print("Please provide the age in number/s")
    myage = str.strip(input())
     
print('You were born in ' + str(2017-int(myage)))
print('You will be ' + str(int(myage)+1) + ' in a year')
if int(myage) < 40:
    print("You are a millenial")
else:
    print("You are not a millenial")
x = 1
while x < 5:
    print("Your age in " + str(2017+ x) +' will be ' + str(int(myage)+x))
    x = x + 1
for i in range(1,5,1):
    print(random.randint(1,2))
    
    
