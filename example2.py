from tkinter import *
root = Tk()
rt = root

btn_column = Button(rt, text="I'm in column 3")
btn_column.grid(column=3)

btn_columnspan = Button(rt, text="I have a columnspan of 3")
btn_columnspan.grid(columnspan=3)

btn_ipadx = Button(rt, text="ipadx of 4")
btn_ipadx.grid(ipadx=4)

btn_ipady = Button(rt, text="ipady of 4")
btn_ipady.grid(ipady=4)

btn_padx = Button(rt, text="padx of 4")
btn_padx.grid(padx=4)

btn_pady = Button(rt, text="pady of 4")
btn_pady.grid(pady=4)

btn_row = Button(rt, text="I'm in row 2")
btn_row.grid(row=2)

btn_rowspan = Button(rt, text="Rowspan of 2")
btn_rowspan.grid(rowspan=2)

btn_sticky = Button(rt, text="I'm stuck to north-east")
btn_sticky.grid(sticky=NE)

rt.mainloop()