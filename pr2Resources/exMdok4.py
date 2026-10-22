from mdokBlocks     import *

print("importing spacy...")
import spacy
print("imported")

################## print similarity##################

def printSim(str1, str2, score):
  print("Similarity between <" + str1 + "> and <" + str2 + ">: " + str(score))

################## main ##################

print("loading spacy model") 
nlp = spacy.load("en_core_web_md")  # or en_core_web_lg
print("model loaded")

mdb = mdokBlocks('sc/2025')

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
  
for i in range(actsLen): 
  for j in range(catsLen):
    actNlp  = actNlps[i]
    catNlp  = catNlps[j]
    actName = actNames[i]
    catName = categories[j]
    simScore = actNlp.similarity(catNlp)
    printSim(actName, catName, score)

### end ###
