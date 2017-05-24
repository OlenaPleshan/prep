#! /bin/bash

ps -ly &> tmpfile.txt
rss=0
# see the explanation why this is done like so
# https://stackoverflow.com/questions/16854280/a-variable-modified-inside-a-while-loop-is-not-remembered
while read -r c1 c2 c3 c4 c5 c6 c7 c8 c9 c10
do 
	let rss+=c8
	echo $rss
# 1d is used to skip the first line
done <<< "$(sed 1d $"tmpfile.txt")"
echo rss=$rss

