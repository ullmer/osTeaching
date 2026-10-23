wget `cat gutEs.url`
grep '/ebooks/' es | sed 's/^.*ebooks\///;s/\".*$//'|grep '^[1-9]'|sort -n | uniq > spanishBookIds.txt
