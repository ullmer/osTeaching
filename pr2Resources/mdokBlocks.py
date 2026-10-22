# Simple class to manage text blocks
# Brygg Ullmer, Clemson University
# Begun 2026-10-20

import traceback
import glob

################## text blocks ##################

class mdokBlocks:
  dirName   = None
  filePat   = '*.txt'
  rfilePat  = '**/*.txt'
  recursive = False #True
  extension = '.txt'
  fileNames = None
  fn2txt    = None
  fn2alias  = None
  verbose   = False

  ################## constructor ##################

  def __init__(self, directoryName, **kwargs):

    self.__dict__.update(kwargs) # allowing (e.g.) -recurive to be passed as an argument

    self.dirName  = directoryName
    self.fn2txt   = {}
    self.fn2alias = {}
    self.findBlockFiles()

  ################## find block files ##################

  def findBlockFiles(self):
    try:
      if self.recursive: globPat = self.dirName + '/' + self.rfilePat
      else:              globPat = self.dirName + '/' + self.filePat

      self.fileNames = glob.glob(globPat, recursive=self.recursive)

    except: print("mdokBlocks readCategories error:"); traceback.print_exc()

  ################## generate filename ##################

  def genFn(self, shortName):
    try:
      result = self.dirName + "/" + shortName + self.extension
      return result
    except: print("mdokBlocks genFns error:"); traceback.print_exc(); return None

  ################## get filenames ##################

  def getFns(self):
    try:
      if self.fileNames is None: print("mdokBlocks getBlockList: no filenames noted!"); return None
      result = self.fileNames
      return result
    except: print("mdokBlocks getBlockList error:"); traceback.print_exc(); return None

  ################## read filename ##################

  def readFn(self, fn, cacheText=True):
    try:
      f          = open(fn, 'rt')
      rawlines   = f.readlines()
      cleanlines = []

      for rawline in rawlines:
        cleanline = rawline.rstrip() 
        cleanlines.append(cleanline)

      if cacheText:
        self.fn2txt[fn] = cleanlines
        
      return cleanlines
    except: print("mdokBlocks readFn error:"); traceback.print_exc(); return None

  ################## read filename by index ##################

  def readFnIdx(self, idx, cacheText=True):
    try:
      fns = self.getFns()
      numFns = len(fns)
      if idx >= numFns: print("mdokBlocks readFnIdx error: index too large"); return None
      fn     =  fns[idx]
      result = self.readFn(fn, cacheText)
      return result

    except: print("mdokBlocks readFnIdx error:"); traceback.print_exc(); return None
  
  ################## load aliases ##################

  def loadAliases(self, aliasFn):
    #e.g.
    #12:Educator Assistance Act
    #15:South Carolina Conservation Education Act

    try:
      f = open(aliasFn, 'rt')
      rawlines = f.readlines()
      for rawline in rawlines:
        cleanline = rawline.rstrip() #remove \n
        colonIdx  = cleanline.find(':')
        if colonIdx < 0: print("loadAliases: ignoring:", cleanline); continue

        shortName = cleanline[0:colonIdx]
        alias     = cleanline[colonIdx+1:]
        fn        = self.genFn(shortName)
        if self.verbose: print("loadAliases:", shortName, alias, fn)
        self.fn2alias[fn] = alias
 
    except: print("mdokBlocks loadAliases error:"); traceback.print_exc(); return None

  ################## get alias by index (alias, fn) ##################

  def getAliasIdxFn(self, idx):
    try:
      if self.fn2alias is None: print("mdokBlocks getAliasIdx uninitialized");
      fakeys = list(self.fn2alias.keys())
      if self.verbose: print("gaif len(fakeys):", len(fakeys))
      fn     = fakeys[idx]
      return fn
    except: print("mdokBlocks getAliasIdxFn error:"); traceback.print_exc(); return None

  def getAliasIdx(self, idx):
    try:
      fn     = self.getAliasIdxFn(idx)
      result = self.fn2alias[fn]
      return result
    except: print("mdokBlocks getAliasIdx error:"); traceback.print_exc(); return None

  def getAliasIdxFA(self, idx):
    try:
      fn     = self.getAliasIdxFn(idx)
      alias  = self.fn2alias[fn]
      result = [fn, alias]
      return result
    except: print("mdokBlocks getAliasIdxFA error:"); traceback.print_exc(); return None

################## main ##################

if __name__ == "__main__":
  mdb = mdokBlocks('sc/2025')
  fl  = mdb.getFns()
  print(fl)

### end ###
