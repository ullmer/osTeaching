## Enodia Scrolling Buttons example
# Brygg Ullmer, Clemson University, and CoPilot
# Begun 2026-11-11

import logging
import tkinter as tk
from tkinter   import ttk
from functools import partial

class EnoScrollingButtons:
  autoBuildUI    = False
  tkRoot         = None
  tkTitle        = 'buttons'
  tkGeom         = "300x700"
  tkCanvas       = None
  tkScroll       = None
  tkContainer    = None
  tkButtonFrame  = None
  tkCanvasWindow = None

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

  ########### mouse wheel ###########
  def mousewheel(self, event):
    canvas = self.tkCanvas
    canvas.yview_scroll(int(-event.delta / 120), "units")

  ########### build ui ###########
  def buildUI(self):
    try:
      # Main container
      container = self.tkContainer = ttk.Frame(root)
      container.pack(fill="both", expand=True)

      # Canvas + scrollbar
      canvas    = self.tkCanvas = tk.Canvas(container)
      scrollbar = self.tkScroll = ttk.Scrollbar(container, orient="vertical", 
        command=canvas.yview)

      canvas.configure(yscrollcommand=scrollbar.set)
      scrollbar.pack(side="right", fill="y")
      canvas.pack(side="left", fill="both", expand=True)

      # Frame that will hold the buttons
      buttonFrame = self.tkButtonFrame = ttk.Frame(canvas)

      # Create a window inside the canvas
      self.tkCanvasWindow = canvas.create_window((0, 0), window=buttonFrame, anchor="nw")
      canvas.bind_all("<MouseWheel>", self.mousewheel)  # Windows/macOS

  ########### on frame configure ###########

  def onFrameConfigure(self, event):
    canvas = self.tkCanvas
    canvas.configure(scrollregion=canvas.bbox("all"))

  ########### on canvas configure ###########

  def onCanvasConfigure(self, event):
    # Keep the internal frame width equal to the canvas width
    canvas       = self.tkCanvas
    canvasWindow = self.tkCanvasWindow
    canvas.itemconfig(canvasWindow, width=event.width)

    self.tkButtonFrame.bind("<Configure>", self.onFrameConfigure)
    self.tkCanvas.bind("<Configure>",      self.onCanvasConfigure)

  ########### add button ###########

  def addButton(self, labelStr, callback):
    btn = ttk.Button(self.tkButtonFrame, text=str(labelStr), command=callback)
    btn.pack(fill="x", padx=2, pady=2)

########## main ########## 

if __name__ == "__main__":
  esb = EnoScrollingButtons(autoBuildUI = True)

  def buttonCb(self, n): print(n) # Button callback

  # Create 30 vertically packed, width-filling buttons
  for i in range(1, 31):
    cb = partial(buttonCb, i)
    esb.addButton(i, cb)

root.mainloop()

### end ###
