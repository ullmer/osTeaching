wget `cat gutEs.url`
grep '/ebooks/' es | sed 's/^.*ebooks\///;s/\".*$//'|sort -n | uniq > spanishBookIds.txt
