from tkinter import *
root = Tk()
rt = root

rt.geometry("500x500")
btn_height = Button(rt, text="50px high")

btn_height.place(height=50, x=200, y=200)
btn_width = Button(rt, text="60px wide")

btn_width.place(width=60, x=300, y=300)
btn_relheight = Button(rt, text="Relheight of 0.6")

btn_relheight.place(relheight=0.6)
btn_relwidth= Button(rt, text="Relwidth of 0.2")

btn_relwidth.place(relwidth=0.2)
btn_relx=Button(rt, text="Relx of 0.3")

btn_relx.place(relx=0.3)
btn_rely=Button(rt, text="Rely of 0.7")

btn_rely.place(rely=0.7)
btn_x=Button(rt, text="X = 400px")

btn_x.place(x=400)
btn_y=Button(rt, text="Y = 321")

btn_y.place(y=321)
rt.mainloop()