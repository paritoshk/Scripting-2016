#! /bin/bash

if [[ -e readme.txt ]] ; then
	echo 'readme.txt already exists. Saving diff with the modified readme'
	diff -u readme.txt modified_readme.txt > readme_diff
else
	echo 'File Readm Does Not Exist! Writing modified_readme to readme'
	cp modified_readme.txt readme.txt
fi

