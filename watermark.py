from tkinter import Tk, Entry, ttk, Label
from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw

# colour schemes
BACKGROUND_COLOUR = "#EADBC8"

# Create the main application window
app = Tk()
app.title("Image watermaker")
app.iconbitmap("images/kanye.ico")
app.geometry("700x650")

frame = Frame(app, borderwidth=2, bg="white", relief=SUNKEN)
frame.pack(side=TOP, fill="x")
# frame.place(anchor="center", relx=0.5, rely=0.5)

app.config(padx=10, pady=10, bg=BACKGROUND_COLOUR)


def add_text():
    """add texts to the image provided"""
    image = Image.open("images/tom6.png")
    text_font = ImageFont.truetype("calibri.ttf", 40)

    text = text_box.get()

    edited_image = ImageDraw.Draw(image)
    edited_image.text((150, 300), text, ("blue"), font=text_font)

    image.save("new_image.png")

    text_box.delete(0, END)
    text_box.insert(0, "Generating watermark...")

    label.after(2000, preview)


def preview():
    """displays the new image"""
    global image_2
    image_2 = PhotoImage(file="new_image.png")
    label.config(image=image_2)

    text_box.delete(0, END)


# Load the image using Pillow
image_path = "image.jpg"
image0 = PhotoImage(file="images/tom.png")
# image = Image.open(image_path)
# image0 = ImageTk.PhotoImage(image)

# Create a label to display the image
label = Label(frame, image=image0)
# label.image = image0  # Keep a reference to the image
# label.grid(row=1, column=2
label.pack()

# Create a text box
text_box = Entry(app, font=("calibri", 25))
# text_box.grid(row=2, column=2)
text_box.pack()

# Create a button to add text to the image
add_text_button = ttk.Button(app, text="Add text to image", command=add_text)
# add_text_button.grid(row=3, column=3)
add_text_button.pack(pady=20)

# Run the application
app.mainloop()
