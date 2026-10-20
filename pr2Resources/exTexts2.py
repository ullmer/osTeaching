from textCategories import *
from textBlocks     import *

################## main ##################

tc = textCategories('cspanCategories.txt')
tb = textBlocks('sc/2025')

cl = tc.getCategoryList()
fl = tb.getFns()

#print('categories:', cl)
#print('text fns:',   fl)

cat0 = tc.getCategoryIdx(0)
cat1 = tc.getCategoryIdx(1)

txt0 = tb.readFnIdx(0)
txt1 = tb.readFnIdx(1)

len0 = len(txt0)
len1 = len(txt1)

for cat  in [cat0, cat1]: print("category:", cat)
for tlen in [len0, len1]: print("text block length:", tlen)

### end ###
