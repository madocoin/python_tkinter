#!\use\bin\python3
import tkinter
from tkinter import Frame
'''simple app Frame with OOP's'''

#create super class pack frame
class tkApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# declaration of application, title, maxsize
App = tkApp()
# here are method calls to the window manager class
App.master.title("the app do no think")
App.master.maxsize(500, 500)
# run the application
App.mainloop()