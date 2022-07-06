from tkinter import *
import random
import pandas

# ------------------------------------------
BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

# sets the words to the users previously studied list
try:
    data = pandas.read_csv("data/words_to_learn.csv")
# if the user doesn't have a previously saved list then it will create a fresh one and orients it accordingly
except FileNotFoundError:
    original_data = pandas.read_csv("data/Quran_Words.csv")
    to_learn = original_data.to_dict(orient="records")
# orients the previously made list into an accessible format if the data was found
else:
    to_learn = data.to_dict(orient="records")


# ----------Card Functionality-------------
# function goes to the next card
def next_card():
    global current_card, flip_timer
    # stops the global timer
    window.after_cancel(flip_timer)
    # finds a new word randomly from the data
    current_card = random.choice(to_learn)
    # changes the word on the canvas to a new one
    # it also changes the language shown, card face, card header, and each font color back to its original side
    canvas.itemconfig(word_text, text=current_card["Arabic"], fill="black")
    canvas.itemconfig(language_text, text="Arabic", fill="black")
    canvas.itemconfig(words_remaining_text, fill="black")
    canvas.itemconfig(card_front, image=card_front_img)
    # starts a new timer for 3 seconds
    flip_timer = window.after(3000, func=flip_card)


# function flips the card
def flip_card():
    global current_card
    # changes the canvas text's language, card face, and font color
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(words_remaining_text, fill="white")
    canvas.itemconfig(card_front, image=card_back_img)


# ----------Button Functionality------------
def known_word():
    global to_learn
    # removes the known word from the csv file
    to_learn.remove(current_card)
    # changes the tracker to accuractly show the amount of words left
    canvas.itemconfig(words_remaining_text, text=f"{len(to_learn)} / 5000")
    print(len(to_learn))
    words_unknown = pandas.DataFrame(to_learn)
    words_unknown.to_csv("data/words_to_learn.csv", index=False)
    # changes the card to the next one
    next_card()


# --------------UI Interface----------------
# creates the window
window = Tk()

# configures the window's background color and added 50 pixel's worth of padding
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

# window title
window.title("Arabic Flashcard App")

flip_timer = window.after(3000, func=flip_card)
# adds a canvas and made the background correspond to the window
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# stores the front card image onto a variable
card_front_img = PhotoImage(file="images/card_front.png")

card_back_img = PhotoImage(file="images/card_back.png")
# adds the front card image to the canvas
card_front = canvas.create_image(400, 263, image=card_front_img)

# sets the location of the canvas within the window
canvas.grid(row=0, column=0, columnspan=2)

# shows the user what the langauge is
language_text = canvas.create_text(400, 130, font=("Arial", 50, "bold"), fill="black")

# shows the user how many words are remaining
words_remaining_text = canvas.create_text(650, 50, text=f"{len(to_learn)} / 5000",
                                          font=("Arial", 30, "bold"), fill="black")

# shows the user the word to translate
word_text = canvas.create_text(400, 280, font=("Arial", 70, "bold"), fill="black")

# creates, configures, and aligns the wrong button on the canvas
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, command=next_card, highlightthickness=0, fg=BACKGROUND_COLOR
                      , highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

# creates, configures, and aligns the right button on the canvas
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, command=known_word, highlightthickness=0, fg=BACKGROUND_COLOR
                      , highlightbackground=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)

# this initializes the first card
next_card()

# this keeps the window open
window.mainloop()
