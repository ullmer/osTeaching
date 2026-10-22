# Example document comparison
# Brygg Ullmer, Clemson University
# Begun 2026-10-22

from mdokMarktime import *
mt = markTime()
from mdokBlocks import *

print(mt.diffstrb(), "importing spacy...")
import spacy
print(mt.diffstrb(), "spacy imported")

################## print similarity##################

def printSim(str1, str2, score):
  print("Similarity between <" + str1 + "> and <" + str2 + ">: " + str(score))

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

for i in range(4): #create NLP instances for named acts/laws
  fn, alias = mdb.getAliasIdxFA(i)
  actStr    = mdb.readFn(fn)
  actNlp    = nlp(actStr)
  actNlps.append(actNlp)
  actNames.append(alias)
  print("alias", alias)
  
for i in range(actsLen): 
  for j in range(catsLen):
    actNlp  = actNlps[i]
    catNlp  = catNlps[j]
    actName = actNames[i]
    catName = categories[j]
    simScore = actNlp.similarity(catNlp)
    printSim(actName, catName, score)

print(mt.diffstr(), "ending")

### end ###
