import os
import shutil
from tkinter import Tk, Canvas, Frame, filedialog, ttk, END, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

BACKGROUND_COLOUR = "#EADBC8"


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermarking App")
        self.final_image = None
        self.temp_image_path = None

        self.frame = Frame(root, width=800, height=800, bg=BACKGROUND_COLOUR)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew", rowspan=9)

        frame = Frame(root)
        frame.grid(padx=20, pady=20)

        self.canvas = Canvas(self.frame, bg="white")
        self.canvas.grid(row=0, column=0, sticky="nsew", rowspan=9)

        self.upload_button = ttk.Button(
            root, text="Upload Image", command=self.upload_image
        )
        self.upload_button.grid(row=9, column=0, pady=10)

        self.add_text_button = ttk.Button(
            root, text="Add watermark", command=self.add_text
        )
        self.add_text_button.grid(row=11, column=1, pady=20, sticky="w")

        self.reset_button = ttk.Button(root, text="Reset", command=self.reset)
        self.reset_button.grid(row=11, column=2, pady=20, padx=(0, 30), sticky="e")

        self.save_button = ttk.Button(root, text="Save Image", command=self.save_image)
        self.save_button.grid(row=11, column=2, pady=20, padx=(0, 30), sticky="e")

        self.text_label = ttk.Label(
            root,
            text="Text",
            background=BACKGROUND_COLOUR,
            font=("calibri", 18, "underline"),
        )
        self.text_label.grid(row=0, column=1, sticky="nsew", pady=(20, 10))

        self.text_box = ttk.Entry(root, font=("calibri", 10), width=33)
        self.text_box.grid(row=1, column=1, columnspan=2, sticky="w")

        self.font_label = ttk.Label(
            root,
            text="Font",
            background=BACKGROUND_COLOUR,
            font=("calibri", 18, "underline"),
        )
        self.font_label.grid(row=7, column=1, pady=10, sticky="nsew")

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
        self.font_dropbox.grid(row=8, column=2, padx=10)

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
        self.font_colour_dropbox.grid(row=9, column=2, padx=10)

        self.transparency_spinbox = ttk.Spinbox(
            root, from_=0, to=100, background=BACKGROUND_COLOUR
        )
        self.transparency_spinbox.set("50")
        self.transparency_spinbox.grid(row=10, column=2, padx=10)

        self.image_on_canvas = None

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
        if not self.final_image:
            print("No image loaded.")
            return

        image = self.final_image.copy()
        img_width, img_height = image.size

        font_name = self.font_dropbox.get().lower() + ".ttf"
        font_path = os.path.join("fonts", font_name)

        try:
            # Calculate text size as a percentage of the image height
            text_size = int(img_height * 0.05)  # e.g., 5% of the image height
            text_font = ImageFont.truetype(font_path, text_size)
        except OSError:
            print(f"Font file {font_path} not found.")
            return

        text = self.text_box.get()
        edited_image = ImageDraw.Draw(image)

        # Calculate position based on the image size
        position = None
        text_position = (
            int(img_width * 0.1),
            int(img_height * 0.9),
        )  # e.g., 10% from the left, 90% from the top
        edited_image.text(text_position, text, fill="blue", font=text_font)

        # Save the watermarked image temporarily
        self.temp_image_path = os.path.join(os.getcwd(), "temp_image.png")
        image.save(self.temp_image_path)

        # Display the updated image on the canvas
        self.display_temp_image(self.temp_image_path)

        self.text_box.delete(0, END)
        self.text_box.insert(0, "Generating watermark...")

    def display_temp_image(self, file_path):
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
        self.canvas.delete("all")
        self.final_image = None
        if self.temp_image_path and os.path.exists(self.temp_image_path):
            os.remove(self.temp_image_path)
        self.temp_image_path = None

    def save_image(self):
        if self.temp_image_path:
            save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            )
            if save_path:
                shutil.copyfile(self.temp_image_path, save_path)
                os.remove(self.temp_image_path)  # Remove temp image after saving
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


if __name__ == "__main__":
    root = Tk()
    root.config(bg=BACKGROUND_COLOUR)
    root.geometry("900x600")
    root.resizable(True, True)
    app = WatermarkApp(root)
    app.run()
