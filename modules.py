#this program imports modules into the program
#modules can be imported like this
#when importing modules in this manner
#youll have to specify the module out of which the function was taken
#in this case it is random.function()
import random
print(str(random.randint(0,69)))

from random import *
print(str(randint(0,69)))
#when importing modules in this manner
#module need not be specified to call the function
#the asteric symbol indicates that everything from the module is imported

import sys
# sys allows us to access sysexit()
print("hello")
sysexit()
#exits the program
print("goodbye")

import pyperclip
#3rd party module
pyperclip.copy()
#copies text to clipboard
pyperclip.paste()
#pastes text from clipboard
               
