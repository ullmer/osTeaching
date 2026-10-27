wget `cat gutMusic.url` -O gut.txt

grep '/ebooks/' gut.txt | sed 's/^.*ebooks\///;s/\".*$//'|grep '^[1-9]' | sort -n | uniq > gutMusic.txt

for i in `seq 26 25 576`

	https://www.gutenberg.org/ebooks/bookshelf/677?start_index=576
do 
  echo $i
  wget `cat gutMusic.url`?start_index=$i -O gut.txt
  grep '/ebooks/' gut.txt | sed 's/^.*ebooks\///;s/\".*$//'|grep '^[1-9]' | sort -n | uniq >> gutMusic.txt
done


