# exTkDualWinPipe1.py

import multiprocessing as mp
import tkinter     as tk
from   tkinter   import ttk

# ---------- Secondary process ----------

def popup_process(conn):
  root = tk.Tk()
  root.title("secondary")
  root.geometry("300x200")

  label = ttk.Label(root, text="secondary window", padding=20)
  label.pack()

  msg_label = ttk.Label(root, text="waiting...")
  msg_label.pack()

  def send_to_main():
    conn.send("hello from secondary")

  ttk.Button(root, text="send to main", command=send_to_main).pack()

  def poll_pipe():
    while conn.poll():
      msg = conn.recv()
      msg_label.config(text=f"rx: {msg}")

    root.after(50, poll_pipe)

  poll_pipe()
  root.mainloop()

############ main #############

def main():
  parent_conn, child_conn = mp.Pipe()

  p = mp.Process(
    target=popup_process,
    args=(child_conn,),
    daemon=True
  )
  p.start()

  root = tk.Tk()
  root.title("main")
  root.geometry("400x300")

  rx_label = ttk.Label(root, text="waiting...")
  rx_label.pack(pady=10)

  def send_to_secondary():
    parent_conn.send("hello from main")

  b = ttk.Button(root, text="send to secondary", command=send_to_secondary)
  b.pack()

  def poll_pipe():
    while parent_conn.poll():
      msg = parent_conn.recv()
      rx_label.config(text=f"rx: {msg}")

    root.after(50, poll_pipe)

  def on_close():
    try: parent_conn.send("__quit__")
    except Exception: pass

    p.terminate()
    root.destroy()

  root.protocol("WM_DELETE_WINDOW", on_close)

  poll_pipe()
  root.mainloop()

if __name__ == "__main__":
  mp.set_start_method("spawn")
  main()

### end ###

