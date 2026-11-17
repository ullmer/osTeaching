"""
Minimal NNG publisher.
"""

import json
import pynng

def main():

  msg = {
      "seq":  1,
      "tags": ["gfx", "scope:sharedCanvas"],
      "data": {
          "scope": "sharedCanvas",
          "updates": ["sq1", "move", [10, 10]]
      }
  }

  with pynng.Pub0(listen="tcp://127.0.0.1:5555") as pub:

    # allow subscribers time to connect
    import time
    time.sleep(0.5)

    pub.send(json.dumps(msg).encode("utf-8"))

if __name__ == "__main__":
  main()

### end ###
