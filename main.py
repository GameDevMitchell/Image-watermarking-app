from tkinter import *

from tkinter import ttk

# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

from PIL import Image, ImageFont, ImageDraw, ImageTk

# colour schemes
BACKGROUND_COLOUR = "#EADBC8"
BUTTON_COLOUR = "#F94892"
CROSS_COLOUR = "#10439F"
CIRCLE_COLOUR = "#F94A29"
NUMERICAL_COLOUR = "#211C6A"


app = Tk()
app.title("Tic-tac-toe")
# app.geometry("900x600")
app.config(padx=30, pady=20, bg=BACKGROUND_COLOUR)


# image1 = Image.open("image1.jpg")
image0 = PhotoImage("image1.jpg")
# photo = ImageTk.PhotoImage(image0)
label = ttk.Label(app, image=image0)
label.grid(row=1, column=2)
# image1.save("image1.jpeg")


# text box
text_box = Entry(app, font=("calibri", 30))
text_box.grid(row=2, column=2)

# add text
add_text_button = ttk.Button(app, text="Add text to image", command=None)
add_text_button.grid(row=3, column=3)
# board image
# board = PhotoImage(file="images/colourful_grid.png")
# image_width = board.width()
# image_height = board.height()

# canvas setup
# max_width = 430
# max_height = 430
# scale = min(max_width / image_width, max_height / image_height)
# image_width = int(image_width * scale)
# image_height = int(image_height * scale)
# board_resized = board.subsample(round(1 / scale), round(1 / scale))

# default canvas
# display_canvas = Canvas(
#     app, width=max_width, height=max_height, bg=BACKGROUND_COLOUR, highlightthickness=0
# )
# display_canvas.create_image(max_width / 2, max_height / 2, image=board_resized)


# play button
# play_image = PhotoImage(file="images/black_play.png")
# play_button = Button(bg=BUTTON_COLOUR, image=play_image, highlightthickness=0)
# play_button.grid(row=2, column=1)

app.mainloop()
