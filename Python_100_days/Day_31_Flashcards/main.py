from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
RANDOM_WORD = {}
TIMER = None
japanese_words_list={}
# ---------------------------- SAVE CARD ------------------------------- #
def remove_recognized():
    japanese_words_list.remove(RANDOM_WORD)
    generate_jap_card()
    data = pandas.DataFrame(japanese_words_list)
    data.to_csv("Python_100_days/Day_31_Flashcards/data/words_to_learn.csv", index=False)

# ---------------------------- ENGLISH CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image,image=card_back)
    canvas.itemconfig(lang_title,text="English",fill="white")
    canvas.itemconfig(lang_word,text=RANDOM_WORD["English"],fill="white")

# ---------------------------- JAPANESE CARD ------------------------------- #
def generate_jap_card():
    global RANDOM_WORD, TIMER
    window.after_cancel(TIMER)
    RANDOM_WORD = random.choice(japanese_words_list)
    print(RANDOM_WORD)
    canvas.itemconfig(canvas_image,image=card_front)
    canvas.itemconfig(lang_title,text="日本語",fill="black")
    canvas.itemconfig(lang_word,text=RANDOM_WORD["Japanese"],fill="black")
    TIMER = window.after(5000,func=flip_card)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Japanese Flashcards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
TIMER = window.after(5000,func=flip_card)

# card front
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="Python_100_days/Day_31_Flashcards/images/card_front.png")
card_back = PhotoImage(file="Python_100_days/Day_31_Flashcards/images/card_back.png")
canvas_image = canvas.create_image(400,263,image=card_front)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
lang_title = canvas.create_text(400,150,text="",font=("Arial", 40,"italic"))
lang_word = canvas.create_text(400,323,text="",font=("Arial", 60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

# button Wrong
image_dont_recognize = PhotoImage(file="Python_100_days/Day_31_Flashcards/images/wrong.png")
button_dont_recognize = Button(image=image_dont_recognize, highlightthickness=0,command=generate_jap_card)
button_dont_recognize.grid(row=1,column=0)

# button Right
image_recongnize = PhotoImage(file="Python_100_days/Day_31_Flashcards/images/right.png")
button_recongnize = Button(image=image_recongnize ,highlightthickness=0,command=remove_recognized) 
button_recongnize.grid(row=1,column=1)

try:
    data = pandas.read_csv("Python_100_days/Day_31_Flashcards/data/words_to_learn.csv")
except FileNotFoundError:    
    data = pandas.read_csv("Python_100_days/Day_31_Flashcards/data/japeng.csv")
    japanese_words_list = data.to_dict(orient="records")
else:    
    japanese_words_list = data.to_dict(orient="records")
   
generate_jap_card()

# button Wrong
window.mainloop()