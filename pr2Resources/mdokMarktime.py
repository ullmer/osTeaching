# Time passage helpers
# Brygg Ullmer, Clemson University
# Begun 2026-10-22

import time

class markTime:
  beginTime = None
  pad       = 4
  lastTime  = None
  def __init__(self): self.beginTime = time.time(); self.lastTime = self.beginTime

  def diff(self):     now = time.time(); diff = now - self.beginTime; return diff
  def diffl(self):    now = time.time(); diff = now - self.lastTime;  self.lastTime=now; return diff
  def diffms(self):   return int(self.diff() *1000)
  def diffmsl(self):  return int(self.diffl()*1000)
  def diffstr(self):  dms  = str(self.diffms());  return dms.rjust(self.pad)
  def diffstrl(self): dms  = str(self.diffmsl()); return dms.rjust(self.pad)
  def diffstrb(self): ds1 = self.diffstr(); ds2 = self.diffstrl(); return (ds1 + " " + ds2)

### end ###
