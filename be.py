import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Line Example with Grid")

# Create a frame to hold the content
frame = tk.Frame(root)
frame.grid(padx=20, pady=20)

# Create a label above the line
label1 = tk.Label(frame, text="Section 1")
label1.grid(row=0, column=0, pady=(0, 10))

# Create a Canvas widget for the line
canvas = tk.Canvas(frame, width=300, height=2, bg="black")
canvas.grid(row=1, column=0, pady=10)

# Draw a line on the canvas (filling the entire width of the canvas)
line = canvas.create_line(0, 1, 300, 1, fill="black")

# Create a label below the line
label2 = tk.Label(frame, text="Section 2")
label2.grid(row=2, column=0, pady=(10, 0))

# Run the application
root.mainloop()
