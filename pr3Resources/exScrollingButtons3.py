## Enodia Scrolling Buttons example
# Brygg Ullmer, Clemson University, and CoPilot
# Begun 2026-11-11

from enoScrollingButtons import *
from mdokCategories import *
from textBlocks     import *

################## main ##################

mc = mdokCategories('cspanCategories.txt')
ml = mc.getCategoryList()

print('categories:', ml)

esb = EnoScrollingButtons(autoBuildUI = True)

def buttonCb(self, n): print(n) # Button callback

# Create 30 vertically packed, width-filling buttons
for i in range(1, 31):
  cb = partial(buttonCb, i)
  esb.addButton(i, cb)

esb.tkRoot.mainloop()

### end ###
