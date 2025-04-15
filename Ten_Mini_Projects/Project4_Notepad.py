import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button

class SimpleNotepad:
    def __init__(self,root: Tk) -> None:
        self.root = root
        self.root.title("My Notepad")
        
        # Text widget
        self.text_area : Text = Text(self.root, wrap ='word')
        self.text_area.pack(expand=True, fill='both')
        
        # Frame
        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()
        
        # Save button
        self.save_button: Button = Button(self.button_frame, text='Save',command=self.save_file)
        self.save_button.pack(side=tk.LEFT)
        
        # Load button
        self.load_button: Button = Button(self.button_frame, text='Load',command=self.load_file)
        self.load_button.pack(side=tk.RIGHT)
        
    def save_file(self) -> None:
        file_path: str = filedialog.asksaveasfilename(defaultextension='.txt',
                                                      filetypes=[('Text files','*.txt')])
        with open(file_path, 'w') as file:
            file.write(self.text_area.get(1.0, tk.END))
            
        print(f'File was save to: {file_path}')
    
    def load_file(self) -> None:
        file_path: str = filedialog.askopenfilename(defaultextension='.txt',
                                                      filetypes=[('Text files','*.txt')])
        with open(file_path, 'r') as file:
            content: str = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.INSERT, content)
            
        print(f'File loaded from: {file_path}')
    
    def run(self) -> None:
        self.root.mainloop()
        
        
def main() -> None:
    root: Tk = Tk()
    app: SimpleNotepad = SimpleNotepad(root=root)
    app.run()
    

if __name__ == '__main__':
    main()
    

# if file exists add text to it without creating a new file each time