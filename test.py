from tkinter import Tk, Canvas, Frame, Button, filedialog, ttk
from tkinter import *
from PIL import Image, ImageTk


# colour schemes
BACKGROUND_COLOUR = "#EADBC8"


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermarking App")

        self.frame = Frame(root, width=800, height=800, bg=BACKGROUND_COLOUR)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew", rowspan=9)

        frame = Frame(root)
        frame.grid(padx=20, pady=20)

        self.canvas = Canvas(self.frame, bg="white")
        self.canvas.grid(row=0, column=0, sticky="nsew", rowspan=9)

        # Buttons
        # upload image button
        self.upload_button = ttk.Button(
            root, text="Upload Image", command=self.upload_image
        )
        self.upload_button.grid(row=9, column=0, pady=10)

        # add text button
        self.add_text_button = ttk.Button(root, text="Add watermark", command=None)
        self.add_text_button.grid(row=11, column=1, pady=20, sticky="w")

        # Reset button
        self.reset_button = ttk.Button(root, text="Reset", command=None)
        self.reset_button.grid(row=11, column=2, pady=20, padx=(0, 30), sticky="e")

        # text label
        self.text_label = ttk.Label(
            root,
            text="Text",
            background=BACKGROUND_COLOUR,
            font=("calibri", 18, "underline"),
        )
        self.text_label.grid(row=0, column=1, sticky="nsew", pady=(20, 10))

        # watermark enrty box
        self.text_box = ttk.Entry(root, font=("calibri", 10), width=33)
        self.text_box.grid(row=1, column=1, columnspan=2, sticky="w")

        # Placement section
        # Placement label
        self.placement_label = ttk.Label(
            root,
            text="Placement",
            background=BACKGROUND_COLOUR,
            font=("calibri", 18, "underline"),
        )
        self.placement_label.grid(row=2, column=1, sticky="nsew", pady=(20, 10))

        # placement configuration
        self.place_label = ttk.Label(
            root,
            text="Placement",
            background=BACKGROUND_COLOUR,
        )
        options = ["Bottom-right", "Bottom-left", "Top-left", "Top-right", "Centre"]
        self.place_dropbox = ttk.Combobox(root, values=options)
        self.place_dropbox.set("Choose placement")
        self.place_label.grid(row=3, column=1, pady=10, sticky="nsew")
        self.place_dropbox.grid(row=3, column=2, padx=10)

        # delta x configuration
        self.delta_x_label = ttk.Label(
            root, text="Delta X (px)", background=BACKGROUND_COLOUR
        )
        self.delta_x_spinbox = ttk.Spinbox(
            root, from_=0, to=10, background=BACKGROUND_COLOUR
        )
        self.delta_x_label.grid(row=4, column=1, pady=10, sticky="nsew")
        self.delta_x_spinbox.grid(row=4, column=2, padx=10)

        # delta y configuration
        self.delta_y_label = ttk.Label(
            root, text="Delta Y (px)", background=BACKGROUND_COLOUR
        )
        self.delta_y_spinbox = ttk.Spinbox(
            root, from_=0, to=10, background=BACKGROUND_COLOUR
        )
        self.delta_y_label.grid(row=5, column=1, pady=10, sticky="nsew")
        self.delta_y_spinbox.grid(row=5, column=2, padx=10)

        # rotation configuration
        self.rotation_label = ttk.Label(
            root, text="Rotation (°)", background=BACKGROUND_COLOUR
        )
        self.rotation_spinbox = ttk.Spinbox(
            root, from_=0, to=360, background=BACKGROUND_COLOUR
        )
        self.rotation_spinbox.set("0")
        self.rotation_label.grid(row=6, column=1, pady=10, sticky="nsew")
        self.rotation_spinbox.grid(row=6, column=2, padx=10)

        # font section
        # font label
        self.font_label = ttk.Label(
            root,
            text="Font",
            background=BACKGROUND_COLOUR,
            font=("calibri", 18, "underline"),
        )
        self.font_label.grid(row=7, column=1, pady=10, sticky="nsew")

        # font type configuration
        self.font_type_label = ttk.Label(
            root, text="Type", background=BACKGROUND_COLOUR
        )
        fonts = [
            "Arial",
            "Helvetica",
            "Times New Roman",
            "Courier New",
            "Verdana",
            "Tahoma",
            "Georgia",
            "Palatino",
            "Garamond",
            "Bookman",
            "Comic Sans MS",
            "Trebuchet MS",
            "Impact",
            "Lucida Sans",
            "Monaco",
            "Consolas",
            "Calibri",
            "Cambria",
            "Candara",
            "Optima",
            "Century Gothic",
            "Franklin Gothic",
            "Gill Sans",
            "Futura",
            "Baskerville",
        ]
        self.font_dropbox = ttk.Combobox(root, values=fonts)
        self.font_dropbox.set("Choose font")
        self.font_type_label.grid(row=8, column=1, pady=10, sticky="nsew")
        self.font_dropbox.grid(row=8, column=2, padx=10)

        # font colour configuartion
        self.font_colour_label = ttk.Label(
            root, text="Type", background=BACKGROUND_COLOUR
        )
        colours = [
            "Red",
            "Green",
            "Blue",
            "Yellow",
            "Purple",
            "Orange",
            "Cyan",
            "Magenta",
            "White",
            "Black",
        ]
        self.font_colour_dropbox = ttk.Combobox(root, values=colours)
        self.font_colour_dropbox.set("Choose colour")
        self.font_colour_label.grid(row=9, column=1, pady=10, sticky="nsew")
        self.font_colour_dropbox.grid(row=9, column=2, padx=10)

        # transparency configuration
        self.transparency_label = ttk.Label(
            root, text="Transparency", background=BACKGROUND_COLOUR
        )
        self.transparency_spinbox = ttk.Spinbox(
            root, from_=0, to=100, background=BACKGROUND_COLOUR
        )
        self.transparency_spinbox.set("50")
        self.transparency_label.grid(row=10, column=1, pady=10, sticky="nsew")
        self.transparency_spinbox.grid(row=10, column=2, padx=10)

        self.image_on_canvas = None

        # Configure grid weights to ensure the canvas expands properly
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def upload_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        if file_path:
            self.display_image(file_path)

    def display_image(self, file_path):
        img = Image.open(file_path)
        img_width, img_height = img.size

        # Calculate the new size preserving the aspect ratio
        frame_width = self.frame.winfo_width()
        frame_height = self.frame.winfo_height()
        ratio = min(frame_width / img_width, frame_height / img_height)
        new_width = int(img_width * ratio)
        new_height = int(img_height * ratio)

        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(resized_img)

        self.canvas.delete("all")
        self.image_on_canvas = self.canvas.create_image(
            frame_width // 2, frame_height // 2, anchor=CENTER, image=self.image_tk
        )

        self.canvas.config(scrollregion=self.canvas.bbox(ALL))


root = Tk()
root.config(bg=BACKGROUND_COLOUR)
root.geometry("900x600")
root.resizable(True, True)
app = WatermarkApp(root)
root.mainloop()
