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
        
        # New button
        self.save_button: Button = Button(self.button_frame, text='New',command=self.new_file)
        self.save_button.pack(side=tk.LEFT)
        
        # Save button
        self.save_button: Button = Button(self.button_frame, text='Save',command=self.save_file)
        self.save_button.pack(side=tk.LEFT)
        
        # Load button
        self.load_button: Button = Button(self.button_frame, text='Load',command=self.load_file)
        self.load_button.pack(side=tk.RIGHT)
        
        # For storing file path and accessing it
        self.current_file = None
        
        # Start notepad with a new file
        self.new_file()
        
    def save_file(self) -> None:
        if not self.current_file:
            file_path: str = filedialog.asksaveasfilename(defaultextension='.txt',
                                                      filetypes=[('Text files','*.txt')])
            self.current_file = file_path
        
        try:
            with open(self.current_file, 'w') as file:
                file.write(self.text_area.get(1.0,tk.END))
        except Exception as e:
            print(e)
            return
                        
        print(f'File was saved to: {self.current_file}')
    
    def load_file(self) -> None:
        file_path: str = filedialog.askopenfilename(defaultextension='.txt',
                                                      filetypes=[('Text files','*.txt')])
        with open(file_path, 'r') as file:
            content: str = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.INSERT, content)
            self.current_file = file_path
            self.root.title(f"My Notepad - {file_path}")
        print(f'File loaded from: {file_path}')
        
    def new_file(self) -> None:
        self.text_area.delete(1.0,tk.END)
        self.current_file = None
        self.root.title(f"My Notepad - Untitled")
        
    def run(self) -> None:
        self.root.mainloop()
        
        
def main() -> None:
    root: Tk = Tk()
    app: SimpleNotepad = SimpleNotepad(root=root)
    app.run()
    

if __name__ == '__main__':
    main()
    

# if file exists add text to it without creating a new file each time