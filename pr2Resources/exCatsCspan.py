# Read in categories for future evolution
# Brygg Ullmer, Clemson University
# Begun 2026-10-20

fn = 'cspanCategories.txt'
f  = open(fn, 'rt')

rawlines   = f.readlines()

entries    = []
categories = {}

for rawline in rawlines:
  cleanline = rawline.rstrip()                     # remove trailing newline character
  if len(cleanline) > 2: 
    entries.append(cleanline) # remove blank lines
    firstColonIndex = cleanline.find(':')
    if firstColonIndex > 0:
      categoryName = cleanline[0:firstColonIndex]
      categories[categoryName] = cleanline

print(list(categories.keys()))

### end ###
