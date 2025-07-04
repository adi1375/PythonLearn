from tkinter import *

def button_clicked():
    new_text= input.get()
    my_label.config(text=new_text)


window =Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

#Label
my_label=Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button'
button = Button(text="Clcik Me", command=button_clicked)
button.grid(column=1,row=1)

button = Button(text="Clcik Me 2", command=button_clicked)
button.grid(column=2,row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)



window.mainloop()