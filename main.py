from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# Accessing data

data = pandas.read_csv("data//french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


# def next_card():
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(canvas_image, image=front_img)
#     canvas.itemconfig(card_title, text="French")
#     canvas.itemconfig(card_word, text=current_card["French"])
#
#     window.after(ms=3000)
#
#     canvas.itemconfig(canvas_image, image=back_img)
#     canvas.itemconfig(card_title, text="English")
#     canvas.itemconfig(card_word, text=current_card["English"])

# Moving to next card word by pressing button
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(ms=3000, func=flip_card)

# Flipping to the English Translation
def flip_card():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# User Interface

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(ms=3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images//card_front.png")
back_img = PhotoImage(file="images//card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images//wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="images//right.png")
known_button = Button(image=check_img, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
