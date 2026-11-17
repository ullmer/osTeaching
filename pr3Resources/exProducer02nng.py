"""
Minimal NNG publisher.
"""

import tkinter as tk
import json
import pynng
  
pub = pynng.Pub0(listen="tcp://127.0.0.1:5555"

msg = {
  "seq":  1,
  "tags": ["gfx", "scope:sharedCanvas"],
  "data": {
    "scope": "sharedCanvas",
    "updates": ["sq1", "move", [10, 10]]
  }
}

pub.send(json.dumps(msg).encode("utf-8"))

### end ###
