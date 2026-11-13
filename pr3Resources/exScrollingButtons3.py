## Enodia Scrolling Buttons example
# Brygg Ullmer, Clemson University, and CoPilot
# Begun 2026-11-11

from enoScrollingButtons import *
from mdokCategories import *
from textBlocks     import *

################## main ##################

esb = EnoScrollingButtons(autoBuildUI = True)
mc  = mdokCategories('cspanCategories.txt')
mcl = mc.getCategoryList()

def buttonCb(self, category): print(category) # Button callback

for category in mcl:
  cb = partial(buttonCb, category)
  esb.addButton(category, cb)

esb.tkRoot.mainloop()

### end ###
