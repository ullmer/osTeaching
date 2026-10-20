from textCategories import *
from textBlocks     import *

################## main ##################

tb = textBlocks('sc/2025')

categories = ['energy', 'education', 'agriculture']

for i in range(4):
  fn, alias = tb.getAliasIdxFA(i)

  for j in categories:

### end ###
