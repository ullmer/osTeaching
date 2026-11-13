# Simple class to manage categories
# Brygg Ullmer, Clemson University
# Begun 2026-10-20

import traceback

################## text categories ##################

class mdokCategories:
  entries    = None
  categories = None

  ################## constructor ##################

  def __init__(self, categoryFn):
    self.readCategories(categoryFn)

  ################## read categories ##################

  def readCategories(self, categoryFn):
    try:
      f  = open(categoryFn, 'rt')
      rawlines   = f.readlines()

      self.entries    = []
      self.categories = {}

      for rawline in rawlines:
        cleanline = rawline.rstrip()                     # remove trailing newline character
        if len(cleanline) > 2: 
          self.entries.append(cleanline) # remove blank lines
          firstColonIndex = cleanline.find(':')
          if firstColonIndex > 0:
            categoryName = cleanline[0:firstColonIndex]
            self.categories[categoryName] = cleanline

    except: print("mdokCategories readCategories error:"); traceback.print_exc()

  ################## get category list ##################

  def getCategoryList(self):
    try:
      if self.categories is None: print("mdokCategories getCategoryList: no categories exist!"); return None
      result = list(self.categories.keys())
      return result
    except: print("mdokCategories getCategoryList error:"); traceback.print_exc(); return None

  ################## get category ##################

  def getCategory(self, categoryName):
    try:
      if self.categories is None:             print("mdokCategories getCategory: no categories exist!"); return None
      if categoryName not in self.categories: print("mdokCategories getCategory: category name not found:", 
                                                    categoryName); return None
      
      result = self.categories[categoryName]
      return result
    except: print("mdokCategories getCategory error:"); traceback.print_exc()

  ################## get category by index ##################

  def getCategoryIdx(self, categoryIdx):
    try:
      if self.categories is None: print("mdokCategories getCategoryIdx: no categories exist!"); return None

      categoryList = self.getCategoryList()
      if categoryList is None: return None

      clLen        = len(categoryList)
      if categoryIdx >= clLen: print("mdokCategories getCategoryIdx: index too large!"); return None
      categoryName = categoryList[categoryIdx]
      result       = self.getCategory(categoryName)
      return result
    except: print("mdokCategories getCategoryIdx error:"); traceback.print_exc()

################## main ##################

if __name__ == "__main__":
  mdc = mdokCategories('cspanCategories.txt')
  cl  = mdc.getCategoryList()
  print(cl)

  cat0 = mdc.getCategoryIdx(0)
  print("\ncategory 0:", cat0)

### end ###
