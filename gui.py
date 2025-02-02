from tkinter import *

window = Tk()

window.title("Welcome to Python GUI")

lblFName = Label(window, text="First Name", font=("Verdana", 15))
lblLName = Label(window, text="Last Name", font=("Verdana", 15))

txtFName = Entry(window)
txtLName = Entry(window)


btnValidate = Button(window, text="Validate")

lblFName.grid(column=0, row=0)
txtFName.grid(column=1, row=0)

lblLName.grid(column=0, row=1)
txtLName.grid(column=1, row=1)

btnValidate.grid(column=0, row=2)

txtFName.focus()

window.geometry("300x300")

window.mainloop()
