# Python 3
"""
from tkinter import *
"""

# Python 2
from Tkinter import *

def openfile():
	print("EEEEEE")

def closefile():
	print("AAAAAA")

def zoomview():
	print("OOOOOOO")

buttonWidth = 20
buttonPadX = 20
buttonPadY = 10
buttonColumnSpan = 2
numButtons = 3
windowPadX = 40
windowPadY = 15
windowWidth = 512
windowHeight = 256

window = Tk()
window.title("Commands")
window.geometry(str(windowWidth) + "x" + str(windowHeight))
canvas = Canvas(window)
canvas.grid(row=0, column=0, padx=windowPadX, pady=windowPadY)

openButton = Button(canvas, text="Open File", width=buttonWidth, command=openfile)
openButton.grid(row=1, column=0, columnspan=buttonColumnSpan, padx=buttonPadX, pady=buttonPadY, sticky=W)
openButton.configure(background="white")

closeButton = Button(canvas, text="Close File", width=buttonWidth, command=closefile)
closeButton.grid(row=2, column=0, columnspan=buttonColumnSpan, padx=buttonPadX, pady=buttonPadY, sticky=W)
closeButton.configure(background="white")

zoomButton = Button(canvas, text="Zoom View", width=buttonWidth, command=zoomview)
zoomButton.grid(row=3, column=0, columnspan=buttonColumnSpan, padx=buttonPadX, pady=buttonPadY, sticky=W)
zoomButton.configure(background="white")

mainloop()

