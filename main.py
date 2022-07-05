from tkinter import *
import random
import pandas

# ------------------------------------------
BACKGROUND_COLOR = "#B1DDC6"


# ----------Card Functionality-------------
def card_change():
    pass


# ----------Button Functionality------------
def wrong_button_func():
    pass


def right_button_func():
    random_int = random.randint(1, 5000)

    data = pandas.read_csv("data/Quran_Words.csv")
    new_word = data._get_value(random_int, "Arabic")
    canvas.itemconfig(word_text, text=f"{new_word}")


# --------------UI Interface----------------
# created the window
window = Tk()

# configured the window's background color and added 50 pixel's worth of padding
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

# window title
window.title("Arabic Flashcard App")

# added a canvas and made the background correspond to the window
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# stored the front card image onto a variable
card_front_img = PhotoImage(file="images/card_front.png")

# added the front card image to the canvas
canvas.create_image(400, 263, image=card_front_img)

# set the location of the canvas within the window
canvas.grid(row=0, column=0, columnspan=2)

# shows the user what the langauge is
language_text = canvas.create_text(400, 130, text="Arabic", font=("Arial", 50, "italic"), fill="black")


# shows the user the word to translate
word_text = canvas.create_text(400, 280, text="Sample", font=("Arial", 70, "bold"), fill="black")

# creates, configures, and aligns the wrong button on the canvas
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, command=wrong_button_func, highlightthickness=0, fg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

# creates, configures, and aligns the right button on the canvas
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, command=right_button_func, highlightthickness=0, fg=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)

# so the window won't close automatically
window.mainloop()
