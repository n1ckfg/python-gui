#import tkinter as tk # Python 3
import Tkinter as tk # Python 2
import threading

# https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop
class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)

        label = tk.Label(self.root, text="Hello World")
        label.pack()

        self.root.mainloop()


app = App()
print("Now we can add more instructions while the gui runs.")

for i in range(10):
    print(i)
