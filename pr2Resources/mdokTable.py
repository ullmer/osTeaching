# Simple class to manage multi-dokument tables
# Brygg Ullmer, Clemson University
# Begun 2026-10-20

import traceback
import tabulate

################## text table ##################

class mdokTable:
  chEmpty  = '·'
  chFilled = '█'

  defaultBarWidth = 5
  defaultTxtPad   = 3

  defaultCols     = 4
  fieldsTop       = []
  fieldsSide      = []

  ################## constructor ##################

  def __init__(self, **kwargs):

    self.__dict__.update(kwargs) # allowing (e.g.) -recurive to be passed as an argument

################## main ##################

if __name__ == "__main__":
  mt = mdokTable('sc/2025')
  #print(fl)

### end ###
