import tkinter as tk
from tkinter import ttk

def open_popup():
  popup = tk.Toplevel(root)
  popup.title("Secondary Window")
  popup.geometry("300x200")
    
  label = ttk.Label(popup, text="toplevel window", padding=20)
  label.pack()
    
  close_btn = ttk.Button(popup, text="close", command=popup.destroy)
  close_btn.pack()

# Main Root Window
root = tk.Tk()
root.title("main")
root.geometry("400x300")

# Button to trigger the popup
open_btn = ttk.Button(root, text="open popup", command=open_popup)
open_btn.pack(expand=True)

root.mainloop()

### end ###
