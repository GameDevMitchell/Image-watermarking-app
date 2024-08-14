import os
import shutil
from tkinter import (
    Canvas,
    Frame,
    filedialog,
    ttk,
    messagebox,
    StringVar,
    END,
    CENTER,
)
from PIL import Image, ImageTk, ImageDraw, ImageFont


# colour schemes
BACKGROUND_COLOUR = "#EADBC8"


class WatermarkApp:
    """Represents a watermark application."""

    def __init__(self, root):
        self.root = root
        self.root.title("Watermarking App")
        self.final_image = None
        self.temp_image_path = None

        self.frame = Frame(root, width=800, height=800, bg=BACKGROUND_COLOUR)
        self.frame.grid(
            row=0, column=0, padx=20, pady=20, sticky="nsew", rowspan=9, columnspan=2
        )

        frame = Frame(root)
        frame.grid(padx=20, pady=20)

        self.canvas = Canvas(self.frame, bg="white")
        self.canvas.grid(row=0, column=0, sticky="nsew", rowspan=9, columnspan=2)

        # Buttons
        # upload image button
        self.upload_button = ttk.Button(
            root, text="Upload Image", command=self.upload_image
        )
        self.upload_button.grid(row=9, column=0)

        # save image button
        self.save_button = ttk.Button(root, text="Save Image", command=self.save_image)
        self.save_button.grid(row=9, column=1, sticky="e", padx=(0, 110))

        # add text button
        self.add_text_button = ttk.Button(
            root, text="Add watermark", command=self.add_text
        )
        self.add_text_button.grid(row=9, column=2, pady=20, sticky="w")

        # Reset button
        self.reset_button = ttk.Button(root, text="Reset", command=self.reset)
        self.reset_button.grid(row=9, column=3, pady=20, padx=(0, 30), sticky="e")

        # text label
        self.text_label = ttk.Label(
            root,
            text="Text",
            background=BACKGROUND_COLOUR,
            font=("calibri", 18, "underline"),
        )
        self.text_label.grid(row=0, column=2, sticky="nsew", pady=(20, 10))

        # watermark enrty box
        self.text_box = ttk.Entry(root, font=("calibri", 10), width=33)
        self.text_box.grid(row=1, column=2, columnspan=2, sticky="w")

        # Placement section
        # Placement label
        self.placement_label = ttk.Label(
            root,
            text="Placement",
            background=BACKGROUND_COLOUR,
            font=("calibri", 18, "underline"),
        )
        self.placement_label.grid(row=2, column=2, sticky="nsew", pady=(20, 10))

        # placement configuration
        self.place_label = ttk.Label(
            root,
            text="Placement",
            background=BACKGROUND_COLOUR,
        )
        options = [
            "Bottom-right",
            "Bottom-left",
            "Top-left",
            "Top-right",
            "Centre",
            "Centre-left",
            "Centre-right",
            "Custom",
        ]

        self.place_var = StringVar()
        self.place_var.set("Choose placement")
        self.place_dropbox = ttk.Combobox(
            root, textvariable=self.place_var, values=options
        )

        self.place_label.grid(row=3, column=2, pady=10, sticky="nsew")
        self.place_dropbox.grid(row=3, column=3, padx=10)

        self.place_var.trace_add("write", self.update_place_dropbox_spinboxes)

        # delta x configuration
        self.delta_x_label = ttk.Label(
            root, text="Delta X (pixels)", background=BACKGROUND_COLOUR
        )
        self.delta_x_spinbox = ttk.Spinbox(
            root, from_=1, to=100, background=BACKGROUND_COLOUR, state="disabled"
        )
        self.delta_x_label.grid(row=4, column=2, pady=10, sticky="nsew")
        self.delta_x_spinbox.set("1")
        self.delta_x_spinbox.grid(row=4, column=3, padx=10)

        # delta y configuration
        self.delta_y_label = ttk.Label(
            root, text="Delta Y (pixels)", background=BACKGROUND_COLOUR
        )
        self.delta_y_spinbox = ttk.Spinbox(
            root, from_=1, to=100, background=BACKGROUND_COLOUR, state="disabled"
        )
        self.delta_y_label.grid(row=5, column=2, pady=10, sticky="nsew")
        self.delta_y_spinbox.set("1")
        self.delta_y_spinbox.grid(row=5, column=3, padx=10)

        # rotation configuration
        self.rotation_label = ttk.Label(
            root, text="Rotation (°)", background=BACKGROUND_COLOUR
        )
        self.rotation_spinbox = ttk.Spinbox(
            root, from_=0, to=360, background=BACKGROUND_COLOUR
        )
        self.rotation_spinbox.set("0")
        # self.rotation_label.grid(row=6, column=1, pady=10, sticky="nsew")
        # self.rotation_spinbox.grid(row=6, column=2, padx=10)

        # font section
        # font label
        self.font_label = ttk.Label(
            root,
            text="Font",
            background=BACKGROUND_COLOUR,
            font=("calibri", 18, "underline"),
        )
        self.font_label.grid(row=6, column=2, pady=10, sticky="nsew")

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
        self.font_type_label.grid(row=7, column=2, pady=10, sticky="nsew")
        self.font_dropbox.grid(row=7, column=3, padx=10)

        # font colour configuartion
        self.font_colour_label = ttk.Label(
            root, text="Colour", background=BACKGROUND_COLOUR
        )
        colours = [
            "AliceBlue",
            "AntiqueWhite",
            "Aqua",
            "Aquamarine",
            "Azure",
            "Beige",
            "Bisque",
            "Black",
            "BlanchedAlmond",
            "Blue",
            "BlueViolet",
            "Brown",
            "BurlyWood",
            "CadetBlue",
            "Chartreuse",
            "Chocolate",
            "Coral",
            "CornflowerBlue",
            "Cornsilk",
            "Crimson",
            "Cyan",
            "DarkBlue",
            "DarkCyan",
            "DarkGoldenRod",
            "DarkGray",
            "DarkGreen",
            "DarkKhaki",
            "DarkMagenta",
            "DarkOliveGreen",
            "DarkOrange",
            "DarkOrchid",
            "DarkRed",
            "DarkSalmon",
            "DarkSeaGreen",
            "DarkSlateBlue",
            "DarkSlateGray",
            "DarkTurquoise",
            "DarkViolet",
            "DeepPink",
            "DeepSkyBlue",
            "DimGray",
            "DodgerBlue",
            "FireBrick",
            "FloralWhite",
            "ForestGreen",
            "Fuchsia",
            "Gainsboro",
            "GhostWhite",
            "Gold",
            "GoldenRod",
            "Gray",
            "Green",
            "GreenYellow",
            "HoneyDew",
            "HotPink",
            "IndianRed",
            "Indigo",
            "Ivory",
            "Khaki",
            "Lavender",
            "LavenderBlush",
            "LawnGreen",
            "LemonChiffon",
            "LightBlue",
            "LightCoral",
            "LightCyan",
            "LightGoldenRodYellow",
            "LightGray",
            "LightGreen",
            "LightPink",
            "LightSalmon",
            "LightSeaGreen",
            "LightSkyBlue",
            "LightSlateGray",
            "LightSteelBlue",
            "LightYellow",
            "Lime",
            "LimeGreen",
            "Linen",
            "Magenta",
            "Maroon",
            "MediumAquaMarine",
            "MediumBlue",
            "MediumOrchid",
            "MediumPurple",
            "MediumSeaGreen",
            "MediumSlateBlue",
            "MediumSpringGreen",
            "MediumTurquoise",
            "MediumVioletRed",
            "MidnightBlue",
            "MintCream",
            "MistyRose",
            "Moccasin",
            "NavajoWhite",
            "Navy",
            "OldLace",
            "Olive",
            "OliveDrab",
            "Orange",
            "OrangeRed",
            "Orchid",
        ]

        self.font_colour_dropbox = ttk.Combobox(root, values=colours)
        self.font_colour_dropbox.set("Choose colour")
        self.font_colour_label.grid(row=8, column=2, pady=10, sticky="nsew")
        self.font_colour_dropbox.grid(row=8, column=3, padx=10)

        # transparency configuration
        self.transparency_label = ttk.Label(
            root, text="Transparency", background=BACKGROUND_COLOUR
        )
        self.transparency_spinbox = ttk.Spinbox(
            root, from_=0, to=100, background=BACKGROUND_COLOUR
        )
        self.transparency_spinbox.set("50")
        # self.transparency_label.grid(row=9, column=1, pady=10, sticky="nsew")
        # self.transparency_spinbox.grid(row=9, column=2, padx=10)

        self.image_on_canvas = None

        # Configure grid weights to ensure the canvas expands properly
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def upload_image(self):
        """Window popup to choose image to upload"""

        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        if file_path:
            self.display_image(file_path)

    def display_image(self, file_path):
        """Displays the image the user chooses to upload"""

        img = Image.open(file_path)
        self.final_image = img
        img_width, img_height = img.size

        frame_width = self.frame.winfo_width()
        frame_height = self.frame.winfo_height()
        ratio = min(frame_width / img_width, frame_height / img_height)
        new_width = int(img_width * ratio)
        new_height = int(img_height * ratio)

        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(resized_img)

        self.canvas.delete("all")
        self.image_on_canvas = self.canvas.create_image(
            frame_width // 2, frame_height // 2, anchor="center", image=self.image_tk
        )

        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def add_text(self):
        """Adds the watermark to the image"""

        # catch errors when adding watermark
        if not self.final_image:
            print("No image loaded.")
            messagebox.showerror(
                "No image loaded", "Please upload an image before adding a watermark"
            )
            return

        if self.place_dropbox.get() == "Choose placement":
            messagebox.showerror(
                "No position chosen", "Please choose a placement option"
            )
            return

        if self.font_dropbox.get() == "Choose font":
            messagebox.showerror("No font chosen", "Please choose a font")
            return

        if self.font_colour_dropbox.get() == "Choose colour":
            messagebox.showerror("No font colour chosen", "Please choose a font colour")
            return

        if self.text_box.get() == "":
            messagebox.showerror("No watermark", "Please type in a watermark")
            return

        image = self.final_image.copy()
        img_width, img_height = image.size

        font_name = self.font_dropbox.get().lower() + ".ttf"
        font_path = os.path.join("fonts", font_name)

        try:
            # Calculate text size as a percentage of the image height
            text_size = int(img_height * 0.05)
            text_font = ImageFont.truetype(font_path, text_size)
        except OSError:
            print(f"Font file {font_path} not found.")
            messagebox.showwarning(
                "Font doesn't exist",
                f"Font file {self.font_dropbox.get()} not found\nTry a different font.",
            )
            return

        text = self.text_box.get()
        edited_image = ImageDraw.Draw(image)

        # Calculating position based on the image size
        position = self.place_dropbox.get()
        coordinates = {
            "Bottom-right": (int(img_width * 0.7), int(img_height * 0.92)),
            "Bottom-left": (int(img_width * 0.3), int(img_height * 0.92)),
            "Top-left": (int(img_width * 0.1), int(img_height * 0.1)),
            "Top-right": (int(img_width * 0.9), int(img_height * 0.1)),
            "Centre": (int(img_width * 0.31), int(img_height * 0.5)),
            "Centre-left": (int(img_width * 0.1), int(img_height * 0.5)),
            "Centre-right": (int(img_width * 0.9), int(img_height * 0.5)),
        }

        if position in coordinates:
            text_position = coordinates[position]
        else:
            xcor = int(self.delta_x_spinbox.get()) / 100
            ycor = int(self.delta_y_spinbox.get()) / 100
            text_position = (
                int(img_width * xcor),
                int(img_height * ycor),
            )

        edited_image.text(
            text_position, text, fill=self.font_colour_dropbox.get(), font=text_font
        )

        # Save the watermarked image temporarily
        self.temp_image_path = os.path.join(os.getcwd(), "temp_image.png")
        image.save(self.temp_image_path)

        # Display the updated image on the canvas
        self.display_temp_image(self.temp_image_path)


    def display_temp_image(self, file_path):
        """Shows a preview of the changes made to the image the user wants to watermark"""

        img = Image.open(file_path)
        img_width, img_height = img.size

        frame_width = self.frame.winfo_width()
        frame_height = self.frame.winfo_height()
        ratio = min(frame_width / img_width, frame_height / img_height)
        new_width = int(img_width * ratio)
        new_height = int(img_height * ratio)

        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(resized_img)

        self.canvas.delete("all")
        self.image_on_canvas = self.canvas.create_image(
            frame_width // 2, frame_height // 2, anchor="center", image=self.image_tk
        )

        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def reset(self):
        """Clears the image in the canvas"""

        self.canvas.delete("all")
        self.final_image = None
        if self.temp_image_path and os.path.exists(self.temp_image_path):
            os.remove(self.temp_image_path)
        self.temp_image_path = None

    def update_place_dropbox_spinboxes(self, *args):
        """activates the placement spinboxes when conditions are satisfied"""

        selected_position = self.place_dropbox.get()
        if selected_position == "Custom":
            self.delta_x_spinbox.configure(state="normal")
            self.delta_y_spinbox.configure(state="normal")
        else:
            self.delta_x_spinbox.configure(state="disabled")
            self.delta_y_spinbox.configure(state="disabled")

    def save_image(self):
        """Saves the watermarked image and opnes it to the user"""

        if self.temp_image_path:
            save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            )
            if save_path:
                shutil.copyfile(self.temp_image_path, save_path)
                os.remove(self.temp_image_path)  # Removes temporary image after saving
                messagebox.showinfo(
                    "Image Saved", f"The image has been saved at:\n{save_path}"
                )
                os.startfile(save_path)
        else:
            messagebox.showwarning(
                "No Watermark", "Please add a watermark before saving the image."
            )

    def run(self):
        self.root.mainloop()
