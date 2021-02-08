from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

#functions
def Calculate():
    miles = float(user_input.get())
    mile = round(miles*1.609)
    km_val.config(text=f"{mile}")


#Entry
user_input = Entry(width=7)
user_input.grid(column=2,row=0)

#label
miles = Label(text="Miles")
miles.grid(column=3,row=0)


mile = 0

Km_display = Label(text=f"is equal to")
Km_display.grid(column=1,row=1)

km_val = Label(text=f"{mile}")
km_val.grid(column=2,row=1)

km = Label(text="Km")
km.grid(column=3,row=1)

#button
button = Button(text="Calculate",command= Calculate)
button.grid(column=2,row=2)



























window.mainloop()