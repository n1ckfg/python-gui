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
        self.buttonWidth = 20
        self.buttonPadX = 20
        self.buttonPadY = 10
        self.buttonColumnSpan = 2
        self.windowPadX = 40
        self.windowPadY = 15
        self.windowWidth = 512
        self.windowHeight = 256

        self.window = self.create_window()
        self.canvas = self.create_canvas()

        self.openButton = self.create_button(self.openfile, "Open File", 1)
        self.closeButton = self.create_button(self.closefile, "Close File", 2)
        self.zoomButton = self.create_button(self.zoomview, "Zoom View", 3)

        self.window.mainloop()

    def create_button(self, command, text="Untitled", row=1, column=0):
        button = tk.Button(self.canvas, text=text, width=self.buttonWidth, command=command)
        button.grid(row=row, column=column, columnspan=self.buttonColumnSpan, padx=self.buttonPadX, pady=self.buttonPadY)#, sticky=tk.W)
        button.configure(background="white")
        return button

    def create_window(self):
        window = tk.Tk()
        window.protocol("WM_DELETE_WINDOW", self.callback)
        window.title("Commands")
        window.geometry(str(self.windowWidth) + "x" + str(self.windowHeight))
        return window

    def create_canvas(self):
        canvas = tk.Canvas(self.window)
        canvas.grid(row=0, column=0, padx=self.windowPadX, pady=self.windowPadY)
        return canvas

    def openfile(self):
        print("EEEEEE")

    def closefile(self):
        print("AAAAAA")

    def zoomview(self):
        print("OOOOOOO")

app = App()

print("Now we can add more instructions while the gui runs.")
