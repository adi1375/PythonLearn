from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Arial", 12,"bold")


# ---------------------------- UI SETUP ------------------------------- #

class DailyExpenses():
    def __init__(self,root: Tk) -> None:
        self.root = root
        self.root.title("Daily Expenses")
        self.root.minsize(height=400,width=400)
        self.root.config(padx=20,pady=20, bg=BACKGROUND_COLOR)
        
        # Balance label
        self.label_balance : Label = Label(text=f"Balance: ", bg=BACKGROUND_COLOR, fg='black',font=FONT)
        self.label_balance.config(padx=5,pady=5)
        self.label_balance.grid(sticky='W', row=0,column=0)
        
        # Display Area
        self.text_area : Text = Text(self.root, height=15, width=60)
        self.text_area.grid(row=1, column=0, columnspan=2)

        
        # Transaction Name/Item
        self.label_name : Label = Label(text="Transaction Name/Item:", bg=BACKGROUND_COLOR,fg='black', font=FONT)
        self.label_name.config(padx=5,pady=10)
        self.label_name.grid(sticky='W',row=2,column=0)

        self.entry_name : Entry = Entry(width=30)
        self.entry_name.focus()
        self.entry_name.grid(sticky='W',row=2,column=1)
        
        # Transaction Amount
        self.label_amount : Label = Label(text="Transaction Amount:", bg=BACKGROUND_COLOR, fg="black", font=FONT)
        self.label_amount.config(padx=5,pady=5)
        self.label_amount.grid(sticky='W',row=3,column=0)

        self.entry_amount : Entry = Entry(width=30)
        self.entry_amount.grid(sticky='W',row=3,column=1)
        
        # Button Add Item
        self.button_add = Button(text="Add", width=20)
        self.button_add.grid(row=4,column=0)
        
        # Button Reset
        self.button_reset = Button(text="Reset", width=20)
        self.button_reset.grid(row=4,column=1,padx=5,pady=10)
        
        # Button Calculate Expenses
        self.button_calculate = Button(text="Calculate", width=55)
        self.button_calculate.grid(row=5,column=0, columnspan=2,padx=5,pady=5)
        
        

        
        
        
        
        
        
        
        
        
    
    
    # Display the program 
    def run(self) -> None:
        self.root.mainloop()
        
        
        
        
def main() -> None:
    root: Tk = Tk()
    app: DailyExpenses = DailyExpenses(root=root)
    app.run()


if __name__ == "__main__":
    main()