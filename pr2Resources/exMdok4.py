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

tb = mdokBlocks('sc/2025')

categories = ['energy', 'education', 'agriculture']
catNlps = []

for cat in categories:
  catNlp = nlp(cat)
  catNlps.append(catNlp)

for i in range(4):
  fn, alias = tb.getAliasIdxFA(i)

  for j in categories:

### end ###
