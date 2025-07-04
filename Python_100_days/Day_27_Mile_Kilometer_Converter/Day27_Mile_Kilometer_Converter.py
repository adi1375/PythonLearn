from tkinter import *

def button_clicked():
    miles= input.get()
    km = float(miles) * 1.60934
    my_label3.config(text=round(km))


window =Tk()
window.title("Mile to Kilometer")
window.config(padx=20, pady=20)

my_label1=Label(text="Miles", font=("Arial", 12, "bold"))
my_label1.grid(row=0,column=2)
my_label2=Label(text="is equal to", font=("Arial", 12, "bold"))
my_label2.grid(row=1,column=0)
my_label3=Label(text="0", font=("Arial", 12, "bold"))
my_label3.grid(row=1,column=1)
my_label4=Label(text="Km", font=("Arial", 12, "bold"))
my_label4.grid(row=1,column=2)

button = Button(text="Calculate", command=button_clicked)
button.grid(row=2,column=1)

input = Entry(width=10)
input.grid(row=0, column=1)


window.mainloop()