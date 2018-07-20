import tkinter as tk # Python 3
#import Tkinter as tk # Python 2

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
windowPadX = 40
windowPadY = 15
windowWidth = 512
windowHeight = 256

# create window
window = tk.Tk()
window.title("Commands")
window.geometry(str(windowWidth) + "x" + str(windowHeight))
canvas = tk.Canvas(window)
canvas.grid(row=0, column=0, padx=windowPadX, pady=windowPadY)

# create buttons
openButton = tk.Button(canvas, text="Open File", width=buttonWidth, command=openfile)
openButton.grid(row=1, column=0, columnspan=buttonColumnSpan, padx=buttonPadX, pady=buttonPadY, sticky=tk.W)
openButton.configure(background="white")

closeButton = tk.Button(canvas, text="Close File", width=buttonWidth, command=closefile)
closeButton.grid(row=2, column=0, columnspan=buttonColumnSpan, padx=buttonPadX, pady=buttonPadY, sticky=tk.W)
closeButton.configure(background="white")

zoomButton = tk.Button(canvas, text="Zoom View", width=buttonWidth, command=zoomview)
zoomButton.grid(row=3, column=0, columnspan=buttonColumnSpan, padx=buttonPadX, pady=buttonPadY, sticky=tk.W)
zoomButton.configure(background="white")

# start the gui
# Note that, without using threading, code placed after this will never run
tk.mainloop()

