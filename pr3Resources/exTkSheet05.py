# https://www.activestate.com/resources/quick-reads/how-to-display-data-in-a-table-using-tkinter/

import tkinter as tk
import tkinter.font as tkfont
import tksheet

top = tk.Tk()
sheet = tksheet.Sheet(top, theme='dark blue')
sheet.grid()
sheet.default_column_width(20)
sheet.set_sheet_data([[f"{ri+cj}" for cj in range(9)] for ri in range(9)])
# table enable choices listed below:
sheet.enable_bindings(("single_select", "row_select",    "column_width_resize", "arrowkeys",
                       "rc_select",     "rc_insert_row", "rc_delete_row",       
                       "copy", "cut", "paste", "delete", "undo", "edit_cell",
                       "right_click_popup_menu"))

sheet.highlight_cells(row=0, column=1, fg="red")

def on_cell_select(event):
  try:
    sel = event.selected
    if sel is not None:
      row, col = sel.row, sel.column
      print(f"selected row={row} column={col}")
      print("=" * 30)

      #sheet.MT.itemconfig(158, fill="red")
      #sheet.MT.itemconfig(158, font=("Calibri", 13, "bold"))

      iid = getCellCanvasTextItem(0, 2)
      sheet.MT.itemconfig(iid, fill="green")
      sheet.MT.itemconfig(iid, font=("Calibri", 13, "bold"))

  except: print("on_cell_select exception")

sheet.extra_bindings([("cell_select", on_cell_select),])

def getCellCanvasTextItem(row, col):
  target = f"{row}_{col}"

  for iid in sheet.MT.find_all():
    if sheet.MT.type(iid) != "text":    continue
    if target in sheet.MT.gettags(iid): return iid
  return None

top.mainloop()

### end ###
