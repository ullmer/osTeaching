### Extract ~keywords from a larger text
# Brygg Ullmer, Clemson University and CoPilot
# Begun 2026-10-23

import traceback
from collections import Counter

class mdokKeywords:
  nlp     = None # externally-initiated spaCy NLP handle
  tokens  = None
  counter = None
  verbose = True
  numKeywords = 100
  
  #### constructor ####

  def __init__(self, nlp, **kwargs):
    self.nlp = nlp
    self.__dict__.update(kwargs) # allowing (e.g.) -recurive to be passed as an argument
  
  def extractKeywords(self, targetText):
    try:
      doc = nlp(targetText)
      self.tokens = []
  
      for token in doc:
        if token.pos_ in ("NOUN", "PROPN") and not token.is_stop:
          self.tokens.append(token.lemma_.lower())
  
  
      self.counter = Counter(self.tokens) 
  
      result = ""
  
      if self.verbose: print("mdokKeywords word counts:")
  
      for word, count in self.counter.most_common(self.numKeywords):
        if self.verbose: print(word, count)
        result += word + "; "

      return result
    except: print("mdokKeywords error:"); traceback.print_exc()
  
### end ###
