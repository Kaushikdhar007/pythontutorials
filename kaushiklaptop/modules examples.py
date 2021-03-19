# Python program to
# demonstrate pyperclip module


# This will import pyperclip
import pyperclip
pyperclip.copy("My name is kaushik dhar")
print(pyperclip.paste())



from emoji import emojize
print(emojize(":kissing_cat:"))
import wikipedia
result = wikipedia.page("2.0")
print(result.summary)

# import antigravity

# This will import
# sys module
# import sys
#
# while True:
# 	print("Type 'exit' to exit")
# 	response = input()
# 	if response == "exit":
# 		print("Exiting the program")
# 		sys.exit()
# 	print("You typed", response)

# This will import urlopen
# class from urllib module


# from urllib.request import urlopen
#
# page = urlopen("https://meet.google.com/mvh-cxjy-vvb?authuser=3")

# Fetches the code
# of the web page
# content = page.read()
#
# print(content)

# This will import turtle module
import turtle


myTurtle = turtle.Turtle()
myWin = turtle.Screen()

# Turtle to draw a spiral
def drawSpiral(myTurtle, linelen):
	myTurtle.forward(linelen)
	myTurtle.right(90)
	drawSpiral(myTurtle, linelen-10)

drawSpiral(myTurtle, 80)
myWin.exitonclick()
