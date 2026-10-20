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
len2 = len(txt2)

for cat  in [cat0, cat1]: print("category:", cat)
for tlen in [len0, len1, len2]: print("text block length:", tlen)

fn0, alias0 = tb.getAliasIdxFA(0)
fn3, alias3 = tb.getAliasIdxFA(2)
print("alias index 0:", alias0, fn0)
print("alias index 3:", alias3, fn3)

### end ###
