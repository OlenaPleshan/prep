#! /bin/bash

for f in /usr/bin/*; do
	if strings $f | grep -q "unable to fork"
	then echo $f
	fi
done
