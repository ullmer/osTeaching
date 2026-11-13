import tkinter as tk
import traceback

from functools import partial # mechanism used to construct callback
from multiprocessing import Process

# ----------------------------------------------------------------------
# Home positions
# ----------------------------------------------------------------------

HOME_GEOMETRIES = {
  "categories":          "200x700+0+50",
  "category_instances":  "200x700+200+50",
  "document_text":       "700x700+400+50",
}

windows = {}

################# maximize window ################# 

def maximize_window(win):
  """Maximize a specific window."""
  try:                win.state("zoomed")             # Windows
  except tk.TclError: win.attributes("-zoomed", True) # Many Linux window managers

################# show all ################# 

def show_all():
  """Restore all windows to their home positions."""
  for name, win in windows.items():
    try: win.state("normal")
    except tk.TclError: pass

    try: win.attributes("-zoomed", False)
    except tk.TclError: pass

    win.geometry(HOME_GEOMETRIES[name])

################# build single-argument callback ################# 

def buildCallback1(methodName, arg1):
  try:    callback = partial(methodName, arg1); return callback
  except: print("buildCallback1 error:"); traceback.print_exc(); return None

################# create window ################# 

def create_window(name, title_text):
  win = tk.Tk()    #win = tk.Toplevel(root)
  win.geometry(HOME_GEOMETRIES[name])
  win.title(title_text)

  # --------------------------------------------------------------
  # Main area (top 500 pixels)
  # --------------------------------------------------------------

  top_frame = tk.Frame(win, height=500)
  top_frame.pack(fill="x")
  top_frame.pack_propagate(False)

  label = tk.Label(top_frame, text=title_text, font=("Arial", 18, "bold"))
  label.pack(expand=True)

  # --------------------------------------------------------------
  # Spacer area
  # --------------------------------------------------------------

  center_frame = tk.Frame(win)
  center_frame.pack(fill="both", expand=True)

  # --------------------------------------------------------------
  # Bottom buttons
  # --------------------------------------------------------------

  button_frame = tk.Frame(win)
  button_frame.pack(side="bottom", fill="x", pady=10)

  maxWinCallback = buildCallback1(maximize_window, win)

  bsa = tk.Button(button_frame, text="show all", command=show_all)
  bmw = tk.Button(button_frame, text="maximize", command=maxWinCallback)

  bsa.pack(side="left",  padx=10)
  bmw.pack(side="right", padx=10)

  windows[name] = win
  win.mainloop()

# ----------------------------------------------------------------------
# Root window (hidden)
# ----------------------------------------------------------------------

if __name__ == '__main__':
  p1 = Process(target=create_window, args=('categories',         'categories'))
  p2 = Process(target=create_window, args=('category_instances', 'category instances'))
  p3 = Process(target=create_window, args=('document_text',      'document text'))

  for p in [p1,p2,p3]: p.start()
  for p in [p1,p2,p3]: p.join()

### end ###

