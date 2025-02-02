from tkinter import *

window = Tk()

window.title("Welcome to Python GUI")

lblFName = Label(window, text="First Name", font=("Verdana", 15))

txtFName = Entry(window)


btnValidate = Button(window, text="Validate")

lblFName.grid(column=0, row=0)
txtFName.grid(column=1, row=0)


btnValidate.grid(column=0, row=1)

txtFName.focus()

window.geometry("300x300")

window.mainloop()
