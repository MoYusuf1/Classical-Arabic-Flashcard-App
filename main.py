from tkinter import *
import random
import pandas

# ------------------------------------------
BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/Quran_Words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


# ----------Card Functionality-------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(word_text, text=current_card["Arabic"], fill="black")
    canvas.itemconfig(language_text, text="Arabic", fill="black")
    canvas.itemconfig(card_front, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(card_front, image=card_back_img)


# ----------Button Functionality------------
def known_word():
    pass


def unknown_word():
    pass


# --------------UI Interface----------------
# created the window
window = Tk()

# configured the window's background color and added 50 pixel's worth of padding
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

# window title
window.title("Arabic Flashcard App")

flip_timer = window.after(3000, func=flip_card)
# added a canvas and made the background correspond to the window
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# stored the front card image onto a variable
card_front_img = PhotoImage(file="images/card_front.png")

card_back_img = PhotoImage(file="images/card_back.png")
# added the front card image to the canvas
card_front = canvas.create_image(400, 263, image=card_front_img)

# set the location of the canvas within the window
canvas.grid(row=0, column=0, columnspan=2)

# shows the user what the langauge is
language_text = canvas.create_text(400, 130, font=("Arial", 40, "bold"), fill="black")

# shows the user the word to translate
word_text = canvas.create_text(400, 280, font=("Arial", 60, "bold"), fill="black")

# creates, configures, and aligns the wrong button on the canvas
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, command=next_card, highlightthickness=0, fg=BACKGROUND_COLOR
                      , highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

# creates, configures, and aligns the right button on the canvas
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, command=next_card, highlightthickness=0, fg=BACKGROUND_COLOR
                      , highlightbackground=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)

# -----------Flipping Mechanism-------------

# so the window won't close automatically

next_card()
window.mainloop()
