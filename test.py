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
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew", rowspan=8)

        frame = Frame(root)
        frame.grid(padx=20, pady=20)

        self.canvas = Canvas(self.frame, bg="white")
        self.canvas.grid(row=0, column=0, sticky="nsew", rowspan=8)

        # upload image button
        self.upload_button = ttk.Button(
            root, text="Upload Image", command=self.upload_image
        )
        self.upload_button.grid(row=1, column=0, pady=10)

        # add text button
        self.add_text_button = ttk.Button(root, text="Add watermark", command=None)
        self.add_text_button.grid(row=2, column=1, pady=10)

        # text label
        self.text_label = ttk.Label(root, text="Text", background=BACKGROUND_COLOUR)
        self.text_label.grid(row=0, column=1, pady=10)

        # watermark enrty box
        self.text_box = ttk.Entry(root, font=("calibri", 10))
        self.text_box.grid(row=1, column=1, pady=10, columnspan=2)

        # Placement label
        self.placement_label = ttk.Label(
            root, text="Placement", background=BACKGROUND_COLOUR
        )
        self.placement_label.grid(row=2, column=1, pady=10)

        # placement configuration
        self.place_label = ttk.Label(
            root, text="Placement", background=BACKGROUND_COLOUR
        )
        options = ["Bottom-right", "Bottom-left", "Top-left", "Top-right", "Centre"]
        self.place_dropbox = ttk.Combobox(root, values=options)
        self.place_label.grid(row=3, column=1, pady=10)
        self.place_dropbox.grid(row=3, column=2, padx=10)

        # delta x configuration
        self.delta_x_label = ttk.Label(root, text="Delta X (px)", background=BACKGROUND_COLOUR)
        self.delta_x_spinbox = ttk.Spinbox(root, from_=0, to=10, background=BACKGROUND_COLOUR)
        self.delta_x_label.grid(row=4, column=1, pady=10)
        self.delta_x_spinbox.grid(row=4, column=2, padx=10)
    
        # delta y configuration
        self.delta_y_label = ttk.Label(root, text="Delta Y (px)", background=BACKGROUND_COLOUR)
        self.delta_y_spinbox = ttk.Spinbox(root, from_=0, to=10, background=BACKGROUND_COLOUR)
        self.delta_y_label.grid(row=5, column=1, pady=10)
        self.delta_y_spinbox.grid(row=5, column=2, padx=10)

        # rotation configuration 
        self.rotation_label = ttk.Label(root, text="Rotation (°)", background=BACKGROUND_COLOUR)
        self.rotation_spinbox = ttk.Spinbox(root, from_=0, to=360, background=BACKGROUND_COLOUR)
        self.rotation_label.grid(row=6, column=1, pady=10)
        self.rotation_spinbox.grid(row=6, column=2, padx=10)


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
root.geometry("800x500")
app = WatermarkApp(root)
root.mainloop()
