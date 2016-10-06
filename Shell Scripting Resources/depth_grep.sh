#! /bin/bash
#A beginner script for wget
cd /tmp
#Goto /tmp

wget -l5 -r www.climagic.org
# Get a fixed-depth files from a website recursively.
#A way of getting all file associations of a HTML document

grep -rnE 'www\..+\..+' www.climagic.org
#match recursively for a web address . Try improving this regex.

rm -fr www.climagic.org
#remove the temp folder.
