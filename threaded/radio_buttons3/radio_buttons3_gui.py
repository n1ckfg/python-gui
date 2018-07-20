import tkinter as tk # Python 3
#import Tkinter as tk # Python 2
import threading

class App(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.window.quit()

    def run(self):
        self.windowWidth = 260
        self.windowHeight = 380
        self.windowPadX = 15
        self.windowPadY = 15

        self.buttonWidth = 20
        self.buttonPadX = 20
        self.buttonPadY = 2
        self.buttonColumnSpan = 2

        self.window = self.create_window()
        self.canvas = self.create_canvas()

        # Assign methods to these buttons in the bridge, where it's easier to access ROS state.
        # Note that Tkinter buttons are numbered from 1.
        self.button1 = self.create_button(None, "Open File", 1) # command, label, index
        self.button2 = self.create_button(None, "Close File", 2)
        self.button3 = self.create_button(None, "Zoom View", 3)

        self.window.mainloop()

    def create_button(self, command=None, text="Untitled", row=1, column=0):
        button = tk.Button(self.canvas, text=text, width=self.buttonWidth, command=command)
        button.grid(row=row, column=column, columnspan=self.buttonColumnSpan, padx=self.buttonPadX, pady=self.buttonPadY)#, sticky=tk.W)
        button.configure(background="white")
        return button

    def create_window(self):
        window = tk.Tk()
        window.protocol("WM_DELETE_WINDOW", self.callback) # cleans up window if it's closed
        window.title("System State")
        window.geometry(str(self.windowWidth) + "x" + str(self.windowHeight))
        return window

    def create_canvas(self):
        canvas = tk.Canvas(self.window)
        canvas.grid(row=0, column=0, padx=self.windowPadX, pady=self.windowPadY)
        return canvas