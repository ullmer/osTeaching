"""
Example threaded enoNngListener usage.
"""

from enoNngListener import *
import time
import sys

def handleMsg(msg):
  print("\nSEQ :", getattr(msg, "seq", None))
  print("DATA:", getattr(msg, "data", None))

listener = enoNngListener(
  endpoint="tcp://127.0.0.1:5555",
  tags=["gfx", "scope:sharedCanvas"],
  callback=handleMsg
)

listener.start()

for i in range(1000):
  print(f"{i} ", end="")
  sys.stdout.flush()
  time.sleep(1.)

listener.stop()

### end ###
