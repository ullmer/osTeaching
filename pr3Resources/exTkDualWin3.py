# exTkDualWinNNG1.py

import multiprocessing as mp
import tkinter         as tk
from   tkinter     import ttk

import pynng

ADDR = "tcp://127.0.0.1:12345"

# --------------------------------------------------
# secondary window process
# --------------------------------------------------

def secondary_process():

  sock = pynng.Pair0()
  sock.dial(ADDR)

  root = tk.Tk()
  root.title("secondary")
  root.geometry("300x200")

  lbl = ttk.Label(root, text="waiting...")
  lbl.pack(pady=10)

  def send_msg():
    sock.send(b"hello from secondary")

  b = ttk.Button(root, text="send to main", command=send_msg)
  b.pack()

  def poll_socket():

    try:
      while True:
        msg = sock.recv(block=False)
        lbl.config(text=f"rx: {msg.decode()}")

    except pynng.TryAgain: pass

    root.after(50, poll_socket)

  poll_socket()
  root.mainloop()


######## main ######## 

def main():

  sock = pynng.Pair0()
  sock.listen(ADDR)

  p = mp.Process(target=secondary_process, daemon=True)
  p.start()

  root = tk.Tk()
  root.title("main")
  root.geometry("400x300")

  lbl = ttk.Label(root, text="waiting...")
  lbl.pack(pady=10)

  def send_msg():
    sock.send(b"hello from main")

  b = ttk.Button(root, text="send to secondary", command=send_msg)
  b.pack()

  def poll_socket():

    try:
      while True:
        msg = sock.recv(block=False)
        lbl.config(text=f"rx: {msg.decode()}")

    except pynng.TryAgain: pass

    root.after(50, poll_socket)

  poll_socket()
  root.mainloop()

if __name__ == "__main__":
  mp.set_start_method("spawn")
  main()

### end ###
