# Simple class to manage categories
# Brygg Ullmer, Clemson University
# Begun 2026-10-20

import traceback

################## text categories ##################

class textCategories:
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

    except: print("textCategories readCategories error:"); traceback.print_exc()

  ################## get category list ##################

  def getCategoryList(self):
    try:
      if self.categories is None: print("textCategories getCategoryList: no categories exist!"); return None
      result = list(self.categories.keys())
      return result
    except: print("textCategories getCategoryList error:"); traceback.print_exc(); return None

  ################## get category ##################

  def getCategory(self, categoryName):
    try:
      if self.categories is None:             print("textCategories getCategory: no categories exist!"); return None
      if categoryName not in self.categories: print("textCategories getCategory: category name not found:", 
                                                    categoryName); return None
      
      result = self.categories[categoryName]
      return result
    except: print("textCategories getCategory error:"); traceback.print_exc()

  ################## get category by index ##################

  def getCategoryIdx(self, categoryIdx):
    try:
      if self.categories is None: print("textCategories getCategoryIdx: no categories exist!"); return None

      categoryList = self.getCategoryList()
      if categoryList is None: return None

      clLen        = len(categoryList)
      if categoryIdx >= clLen: print("textCategories getCategoryIdx: index too large!"); return None
      categoryName = categoryList[categoryIdx]
      result       = self.getCategory(categoryName)
      return result
    except: print("textCategories getCategoryIdx error:"); traceback.print_exc()

################## main ##################

if __name__ == "__main__":
  tc = textCategories('cspanCategories.txt')
  cl = tc.getCategoryList()
  print(cl)

  cat0 = tc.getCategoryIdx(0)
  print("\ncategory 0:", cat0)

### end ###
