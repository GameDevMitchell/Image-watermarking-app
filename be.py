import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create two buttons
button1 = ttk.Button(root, text="Button 1")
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = ttk.Button(root, text="Button 2")
button2.grid(row=1, column=0, padx=10, pady=0)  # No padding

root.mainloop()
