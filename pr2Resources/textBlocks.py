# Simple class to manage text blocks
# Brygg Ullmer, Clemson University
# Begun 2026-10-20

import traceback
import glob

################## text blocks ##################

class textBlocks:
  dirName   = None
  filePat   = '*.txt'
  extension = '.txt'
  fileNames = None
  fn2txt    = None

  ################## constructor ##################

  def __init__(self, directoryName):
    self.dirName   = directoryName
    self.fn2txt = {}
    self.findBlockFiles()

  ################## find block files ##################

  def findBlockFiles(self):
    try:
      globPat = self.dirName + '/' + self.filePat
      self.fileNames = glob.glob(globPat)

    except: print("textBlocks readCategories error:"); traceback.print_exc()

  ################## generate filename ##################

  def genFn(self, shortName):
    try:
      result = self.dirName + "/" + shortName + self.extension
      return result
    except: print("textBlocks genFns error:"); traceback.print_exc(); return None

  ################## get filenames ##################

  def getFns(self):
    try:
      if self.fileNames is None: print("textBlocks getBlockList: no filenames noted!"); return None
      result = self.fileNames
      return result
    except: print("textBlocks getBlockList error:"); traceback.print_exc(); return None

  ################## read filename ##################

  def readFn(self, fn, cacheText=True):
    try:
      f     = open(fn, 'rt')
      lines = f.readlines()
      if cacheText:
        self.fn2txt[fn] = lines
        
      return lines
    except: print("textBlocks readFn error:"); traceback.print_exc(); return None

  ################## read filename by index ##################

  def readFnIdx(self, idx, cacheText=True):
    try:
      fns = self.getFns()
      numFns = len(fns)
      if idx >= numFns: print("textBlocks readFnIdx error: index too large"); return None
      fn     =  fns[idx]
      result = self.readFn(fn, cacheText)
      return result

    except: print("textBlocks readFnIdx error:"); traceback.print_exc(); return None

################## main ##################

if __name__ == "__main__":
  tb = textBlocks('sc/2025')
  fl = tb.getFns()
  print(fl)

### end ###
