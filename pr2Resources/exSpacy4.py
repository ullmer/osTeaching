print("importing spacy")
import spacy
from mdokKeywords import *
from mdokBlocks   import *

print("loading spacy model") 
nlp = spacy.load("en_core_web_md")  # or en_core_web_lg
print("model loaded")

mdb       = mdokBlocks("sc")
sc2025_41a = mdb.readFn("sc/2025/41.txt")
sc2025_41b = " ".join(sc2025_41a)

mdkw = mdokKeywords(nlp)
kw   = mdkw.extractKeywords(sc2025_41b)

print("\n\n" + str(kw))


### end ###

