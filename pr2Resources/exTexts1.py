from textCategories import *
from textBlocks     import *

################## main ##################

tc = textCategories('cspanCategories.txt')
tb = textBlocks('sc/2025')

cl = tc.getCategoryList()
bl = tb.getFns()

print('categories:', cl)
print('text fns:',   bl)

### end ###
