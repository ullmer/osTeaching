import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("30 Buttons")
root.geometry("300x700")

# Main container
container = ttk.Frame(root)
container.pack(fill="both", expand=True)

# Canvas + scrollbar
canvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)

canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Frame that will hold the buttons
button_frame = ttk.Frame(canvas)

# Create a window inside the canvas
canvas_window = canvas.create_window(
    (0, 0),
    window=button_frame,
    anchor="nw"
)

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_canvas_configure(event):
    # Keep the internal frame width equal to the canvas width
    canvas.itemconfig(canvas_window, width=event.width)

button_frame.bind("<Configure>", on_frame_configure)
canvas.bind("<Configure>", on_canvas_configure)

# Button callback
def button_pressed(n):
    print(n)

# Create 30 vertically packed, width-filling buttons
for i in range(1, 31):
    btn = ttk.Button(
        button_frame,
        text=str(i),
        command=lambda n=i: button_pressed(n)
    )
    btn.pack(fill="x", padx=2, pady=2)

# Optional mouse wheel support
def mousewheel(event):
    canvas.yview_scroll(int(-event.delta / 120), "units")

canvas.bind_all("<MouseWheel>", mousewheel)  # Windows/macOS

root.mainloop()

