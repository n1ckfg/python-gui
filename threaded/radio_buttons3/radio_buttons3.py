from radio_buttons3_gui import *

def print_text(text):
    print(text)

guiIsConfigured = False

app = App()

while (guiIsConfigured == False):
    try:
        app.button1.configure(command=lambda:print_text("EEEEEE"))
        app.button2.configure(command=lambda:print_text("IIIIII"))
        app.button3.configure(command=lambda:print_text("AAAAAA"))
        guiIsConfigured = True
    except:
        guiIsConfigured = False

print("Now we can add more instructions while the gui runs.")
