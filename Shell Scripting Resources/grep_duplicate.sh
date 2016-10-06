
#!/bin/bash

#Rudimentry implementation of grep

if [ -z "$1" ]
then
  echo "Incorrect Number of Arguments . One Permitted"
  exit 1
fi
for file in *
do
  output=$(sed -n /"$1"/p $file)
  if [ ! -z "$output" ]
  then
    echo -n "$file: "
    echo "$output"
  fi
  echo
done

exit 0
