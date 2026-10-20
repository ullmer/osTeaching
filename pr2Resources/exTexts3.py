from textCategories import *
from textBlocks     import *

################## main ##################

tc = textCategories('cspanCategories.txt')
tb = textBlocks('sc/2025')

tb.loadAliases('sc25-aliases.txt')
cl = tc.getCategoryList()
fl = tb.getFns()

#print('categories:', cl)
#print('text fns:',   fl)

cat0 = tc.getCategoryIdx(0)
cat1 = tc.getCategoryIdx(1)

txt0 = tb.readFnIdx(0)
txt1 = tb.readFnIdx(1)
txt2 = tb.readFnIdx(2)

len0 = len(txt0)
len1 = len(txt1)
len2 = len(txt1)

for cat  in [cat0, cat1]: print("category:", cat)
for tlen in [len0, len1, len2]: print("text block length:", tlen)

aif0 = tb.getAliasIdxFn(0)
print("alias index filename 0:", aif0)

### end ###
