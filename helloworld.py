#!\use\bin\python3
from tkinter import Tk
from tkinter import ttk
#window tkinter
root = Tk()
#add window to frame
frame = ttk.Frame(root, padding=280)
frame.grid()
ttk.Label(frame, text="Hello World!").grid(column=0, row=0)
ttk.Button(frame, text="exit", command=root.destroy).grid(column=0, row=1)
#run app (mainloop)
root.mainloop()