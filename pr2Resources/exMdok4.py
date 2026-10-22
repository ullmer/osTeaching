from mdokBlocks     import *
import spacy

################## print similarity##################

def printSim(str1, str2, score):
  print("Similarity between <" + str1 + "> and <" + str2 + ">: " + str(score))

score = doc1.similarity(doc2)
printSim(str1, str2, score)

################## main ##################

print("loading spacy model") 
nlp = spacy.load("en_core_web_md")  # or en_core_web_lg
print("model loaded")

mdb = mdokBlocks('sc/2025')

categories = ['energy', 'education', 'agriculture']
catsLen    = len(categories)
actsLen    = 4
catsNlps   = []
actsNlps   = []

for cat in categories: #create NLP instances for categories
  catNlp = nlp(cat)
  catNlps.append(catNlp)

for i in range(4): #create NLP instances for named acts/laws
  fn, alias = tb.getAliasIdxFA(i)
  actStr = mdb.readFn(fn)
  actNlp = nlp(actStr)
  actNlps.append(actNlp)
  
for i in range(actsLen): 
  for j in range(catsLen):
    actNlp = ac

### end ###
