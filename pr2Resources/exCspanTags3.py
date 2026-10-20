import yaml
import glob
import traceback

fn='cspan-tags.yaml'
f =open(fn, 'rt')
yd=yaml.safe_load(f)

tags = yd['tags']
#print("Tags:", tags)

hashstr = '#' * 10

for tag in tags:
  try:
    taggedList    = tags[tag]
    taggedListLen = len(taggedList)
    catName       = taggedList[0]['catName']
    catStr = catName + ". "

    #print(hashstr, tag, ':', catName, hashstr)

    for i in range(1, taggedListLen):
      tagEl   = taggedList[i]
      tagName = tagEl['name']
      catStr += tagName + ". "

    print(catStr + "\n")

  except: print(">> ignoring tag", tag); traceback.print_exc()

### end ###
