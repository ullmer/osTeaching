# Simple class to manage categories
# Brygg Ullmer, Clemson University
# Begun 2026-10-20

################## text categories ##################

class textCategories:
  entries    = None
  categories = None

  def __init__(categoryFn):
    self.readCategories(categoryFn)

  def readCategories(categoryFn):
    try:
      f  = open(categoryFn, 'rt')
      rawlines   = f.readlines()

      self.entries    = []
      self.categories = {}

      for rawline in rawlines:
        cleanline = rawline.rstrip()                     # remove trailing newline character
        if len(cleanline) > 2: 
          entries.append(cleanline) # remove blank lines
          firstColonIndex = cleanline.find(':')
          if firstColonIndex > 0:
            categoryName = cleanline[0:firstColonIndex]
            categories[categoryName] = cleanline

################## main ##################

if __name__ == "__main__":
  tc = textCategories('cspanCategories.txt')
  cl = tc.getCategoryList()
  print(cl)

### end ###
