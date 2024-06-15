import tkinter as tk
from tkinter import ttk

class WatermarkApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Watermark Position Selector")
        self.geometry("400x200")

        self.x_spinbox = tk.Spinbox(self, from_=0, to=100, state="disabled")
        self.x_spinbox.pack(pady=5)

        self.y_spinbox = tk.Spinbox(self, from_=0, to=100, state="disabled")
        self.y_spinbox.pack(pady=5)

        self.position_var = tk.StringVar()
        self.position_var.set("Top Left")

        self.position_dropdown = ttk.Combobox(self, textvariable=self.position_var, state="readonly")
        self.position_dropdown.pack(pady=5)
        self.position_dropdown.bind("<<ComboboxSelected>>", self.update_spinboxes)

        self.position_var.trace_add("write", self.update_spinboxes)

        self.position_dropdown["values"] = ["Top Left", "Top Right", "Custom"]

    def update_spinboxes(self, *args):
        selected_position = self.position_var.get()
        if selected_position == "Custom":
            self.x_spinbox.configure(state="normal")
            self.y_spinbox.configure(state="normal")
        else:
            self.x_spinbox.configure(state="disabled")
            self.y_spinbox.configure(state="disabled")

if __name__ == "__main__":
    app = WatermarkApp()
    app.mainloop()
