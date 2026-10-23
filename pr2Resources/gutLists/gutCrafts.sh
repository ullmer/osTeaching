wget `cat gutCrafts.url` -O gut.txt

grep '/ebooks/' gut.txt | sed 's/^.*ebooks\///;s/\".*$//'|grep '^[1-9]' | sort -n | uniq > gutCrafts.txt

for i in 26 51 76
do 
  echo $i
  wget `cat gutCrafts.url`?start_index=$i -O gut.txt
  grep '/ebooks/' gut.txt | sed 's/^.*ebooks\///;s/\".*$//'|grep '^[1-9]' | sort -n | uniq >> gutCrafts.txt
done


