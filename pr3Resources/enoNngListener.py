"""
Threaded callback-based NNG listener.
Port of enoPlasmiteListener.py

Brygg Ullmer + Copilot
"""

import threading
import logging
import traceback
import json
from types import SimpleNamespace

import pynng

class enoNngListener:

  endpoint  = "tcp://127.0.0.1:5555"
  thread    = None
  running   = False
  callback  = None
  ready     = None
  tags      = None

  ########### constructor ###########

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs)

    self.running = False
    self.ready   = threading.Event()

    logging.basicConfig(level=logging.INFO)
    self.logger = logging.getLogger(__name__)

  ########### log error ###########

  def logErr(self, msg):
    try:
      self.logger.error(msg)
      traceback.print_exc()
    except:
      traceback.print_exc()

  ########### log info ###########

  def logInf(self, msg):
    try:
      self.logger.info(msg)
    except:
      traceback.print_exc()

  ########### tag match ###########

  def tagMatch(self, msg_tags):
    if not self.tags:
      return True

    return all(tag in msg_tags for tag in self.tags)

  ########### _listen ###########

  def _listen(self):

    try:
      sock = pynng.Sub0()

      sock.dial(self.endpoint)

      # receive everything
      sock.subscribe(b"")

      self.logger.info(f"Connected to {self.endpoint}")

      self.ready.set()

      while self.running:

        try:
          payload = sock.recv()

          obj = json.loads(
            payload.decode("utf-8"),
            object_hook=lambda d: SimpleNamespace(**d)
          )

          msg_tags = getattr(obj, "tags", [])

          if self.tagMatch(msg_tags):

            if self.callback:
              self.callback(obj)

        except Exception:
          traceback.print_exc()

    except Exception:
      self.logErr("_listen setup issue")

  ########### start ###########

  def start(self):

    if not self.running:
      self.running = True
      self.thread  = threading.Thread(target=self._listen, daemon=True)
      self.thread.start()

    self.ready.wait(timeout=1.0)

  ########### stop ###########

  def stop(self):
    self.running = False
    if self.thread: self.thread.join(timeout=1.0)
    self.logger.info("enoNngListener stopped")

  ########### append ###########

  def append(self, data):
    with pynng.Pub0() as sock:
      sock.dial(self.endpoint)
      if isinstance(data, dict):
        data = json.dumps(data)

      sock.send(data.encode("utf-8"))

### end ###
