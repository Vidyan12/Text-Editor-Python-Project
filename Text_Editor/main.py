import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file for editing."""
    file_path = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return
    text_edit.delete(1.0, tk.END)
    with open(file_path, "r") as input_file:
        content = input_file.read()
        text_edit.insert(tk.END, content)
    window.title(f"Text Editor - {file_path}")

def save_file():
    """Save the current content as a new file."""
    file_path = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not file_path:
        return
    with open(file_path, "w") as output_file:
        content = text_edit.get(1.0, tk.END)
        output_file.write(content)
    window.title(f"Text Editor - {file_path}")

# Create the main window
window = tk.Tk()
window.title("TextEditor Pro!!!")
window.geometry("800x600")

# Set custom icon (replace 'your_icon.ico' with the path to your icon file)
window.iconbitmap('icon.ico')


# Text widget for editing
text_edit = tk.Text(window, wrap="word")
text_edit.grid(row=0, column=1, sticky="nsew")

# Frame for buttons
button_frame = tk.Frame(window, relief=tk.RAISED, bd=2)
button_frame.grid(row=0, column=0, sticky="ns")

# Open button
btn_open = tk.Button(button_frame, text="Open", command=open_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

# Save button
btn_save = tk.Button(button_frame, text="Save As...", command=save_file)
btn_save.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

# Configure grid weights
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# Start the Tkinter event loop
window.mainloop()
