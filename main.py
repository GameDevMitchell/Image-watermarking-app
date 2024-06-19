from tkinter import PhotoImage, Tk
from watermarker import WatermarkApp

BACKGROUND_COLOUR = "#EADBC8"

root = Tk()
icon = PhotoImage(file="images\icons\icon2.png")
root.iconphoto(False, icon)
root.config(bg=BACKGROUND_COLOUR)

# optional window size
# root.geometry("900x600")

# root.resizable(True, True)
app = WatermarkApp(root)
app.run()
