# Simple class to manage text blocks
# Brygg Ullmer, Clemson University
# Begun 2026-10-20

import traceback
import glob

################## text blocks ##################

class textBlocks:
  dirName   = None
  filePat   = '*.txt'
  fileNames = None

  def __init__(self, directoryName):
    self.dirName = directoryName
    self.findBlockFiles()

  def findBlockFiles(self):
    try:
      globPat = self.dirName + '/' + self.filePat
      self.fileNames = glob.glob(globPat)

    except: print("textBlocks readCategories error:"); traceback.print_exc()

  def getBlockList(self):
    try:
      if self.fileNames is None: print("textBlocks getBlockList: no filenames noted!"); return None
      result = self.fileNames
      return result
    except: print("textBlocks getBlockList error:"); traceback.print_exc()

################## main ##################

if __name__ == "__main__":
  tb = textBlocks('sc/2025')
  bl = tb.getBlockList()
  print(bl)

### end ###
