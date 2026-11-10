import tkinter as tk

# ----------------------------------------------------------------------
# Home positions
# ----------------------------------------------------------------------

HOME_GEOMETRIES = {
  "categories":          "200x700+0+50",
  "category_instances":  "200x700+200+50",
  "document_text":       "700x700+400+50",
}

windows = {}

def maximize_window(win):
  """Maximize a specific window."""
  try:
      # Windows
      win.state("zoomed")
  except tk.TclError:
      # Many Linux window managers
      win.attributes("-zoomed", True)


def show_all():
  """Restore all windows to their home positions."""
  for name, win in windows.items():
      try:
          win.state("normal")
      except tk.TclError:
          pass

      try:
          win.attributes("-zoomed", False)
      except tk.TclError:
          pass

      win.geometry(HOME_GEOMETRIES[name])


def create_window(name, title_text):
  win = tk.Toplevel(root)
  win.geometry(HOME_GEOMETRIES[name])
  win.title(title_text)

  # --------------------------------------------------------------
  # Main area (top 500 pixels)
  # --------------------------------------------------------------

  top_frame = tk.Frame(win, height=500)
  top_frame.pack(fill="x")
  top_frame.pack_propagate(False)

  label = tk.Label(
      top_frame,
      text=title_text,
      font=("Arial", 18, "bold")
  )
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

  tk.Button(
      button_frame,
      text="show all",
      command=show_all
  ).pack(side="left", padx=10)

  tk.Button(
      button_frame,
      text="maximize",
      command=lambda w=win: maximize_window(w)
  ).pack(side="right", padx=10)

  windows[name] = win
  return win


# ----------------------------------------------------------------------
# Root window (hidden)
# ----------------------------------------------------------------------

root = tk.Tk()
root.withdraw()

create_window("categories", "categories")
create_window("category_instances", "category instances")
create_window("document_text", "document text")

root.mainloop()
