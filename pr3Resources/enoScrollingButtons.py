## Enodia Scrolling Buttons example
# Brygg Ullmer, Clemson University, and CoPilot
# Begun 2026-11-11

import logging
import tkinter as tk
from tkinter import ttk

class enoScrollingButtons:
  autoBuildUI = False
  tkRoot      = None
  tkTitle     = 'buttons'
  tkGeom      = "300x700"
  tkCanvas    = None
  tkContainer = None

 ########### constructor ###########
  def __init__(self, **kwargs):
    self.__dict__.update(kwargs)
    logging.basicConfig(level=logging.INFO)
    self.logger = logging.getLogger(__name__)

    if self.autoBuildUI: self.buildUiRoot(); self.buildUI()

  ########### log error ###########
  def logErr(self, msg):
    try:    self.logger.error(msg); traceback.print_exc()
    except: print("logErr error:"); traceback.print_exc()

  ########### log info ###########
  def logInf(self, msg):
    try:    self.logger.info(msg)
    except: print("logInf error:"); traceback.print_exc()

  ########### build ui root ###########
  def buildUiRoot(self):
    root = self.tkRoot = tk.Tk()
    root.title(self.tkTitle)
    root.geometry(self.tkGeom)

  ########### build ui ###########
  def buildUI(self):
    try:
      # Main container
      container = self.tkContainer = ttk.Frame(root)
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

### end ###
