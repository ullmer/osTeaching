"""
Minimal NNG publisher.
"""

import tkinter as tk
import json
import pynng
import sys
  
pub = pynng.Pub0(listen="tcp://127.0.0.1:5555")

msg = {
  "seq":  1,
  "tags": ["gfx", "scope:sharedCanvas"],
  "data": {
    "scope": "sharedCanvas",
    "updates": ["sq1", "move", [10, 10]]
  }
}

def sendCb():
  global tk

def exitCb(): sys.exit(1)

root = tk.Tk()
root.title("nng send ex01")

b1 = tk.Button(text="send via nng", command=sendCb)
b2 = tk.Button(text="quit",         command=exitCb)
for b in [b1, b2]: b.pack()

pub.send(json.dumps(msg).encode("utf-8"))

root.mainloop()

### end ###
