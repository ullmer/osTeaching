# Example document comparison
# Brygg Ullmer, Clemson University
# Begun 2026-10-22

from mdokMarktime import *
mt = markTime()
from mdokBlocks import *

print(mt.diffstrb(), "importing spaCy...")
import spacy
print(mt.diffstrb(), "spaCy imported")

################## print similarity##################

def printSim(str1, str2, score):
  strScore  = str(int(score*1000))
  strLabel  = ": similarity between <" + str1 + "> and <" + str2 + ">"
  print(strScore, strLabel)

################## main ##################

print(mt.diffstrb(), "loading spacy model") 
nlp = spacy.load("en_core_web_md")  # or en_core_web_lg
print(mt.diffstrb(), "model loaded")

mdb = mdokBlocks('sc/2025')
mdb.loadAliases('sc25-aliases.txt')

categories = ['energy', 'education', 'agriculture']
catsLen    = len(categories)
actsLen    = 4
catNlps   = []
actNlps   = []
actNames  = []

for cat in categories: #create NLP instances for categories
  catNlp = nlp(cat)
  catNlps.append(catNlp)

print(mt.diffstrb(), "creating NLP instances of acts")
for i in range(4): #create NLP instances for named acts/laws
  fn, alias = mdb.getAliasIdxFA(i)
  actStrs   = mdb.readFn(fn)
  actStr    = " ".join(actStrs) # join list of strings into single string
  actNlp    = nlp(actStr)
  actNlps.append(actNlp)
  actNames.append(alias)
  print(mt.diffstrb(), "created nlp for", alias)
  
for i in range(actsLen): 
  for j in range(catsLen):
    actNlp  = actNlps[i]
    catNlp  = catNlps[j]
    actName = actNames[i]
    catName = categories[j]
    simScore = actNlp.similarity(catNlp)
    printSim(actName, catName, simScore)
  print("---")

print(mt.diffstrb(), "ending")

### end ###
