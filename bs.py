import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Spinbox Example")

# Create a frame to hold the content
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill=tk.BOTH, expand=True)

# Label to indicate the purpose of the Spinbox
label = tk.Label(frame, text="Select a number:")
label.pack(pady=5)

# Create a Spinbox widget
spinbox = tk.Spinbox(frame, from_=0, to=10)
spinbox.pack(pady=5)

# Function to handle the value change event
def on_spinbox_change():
    selected_value = spinbox.get()
    print(f"Selected value: {selected_value}")

# Bind the value change event to the function
spinbox.config(command=on_spinbox_change)

# Run the application
root.mainloop()
