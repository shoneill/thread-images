#!/bin/bash

# main script

PWD=`pwd`

# format the destination for PNGs

if [ $# -eq 0 ]
then 
    echo "Please specify a 4chan thread URL"
    exit 1
elif [ $# -eq 1 ]
then
    DEST=$PWD/`date +%Y%m%d%H%M`
    mkdir $DEST
    wget -q -O $DEST/temp-html $1
elif [ $# -eq 2 ]
then
    DEST=$1
    if [ ! -d "$DEST" ]
    then
        mkdir -p $DEST
    fi
    wget -q -O $DEST/temp-html $2
else
    echo "too many arguements"
    exit 1
fi

# get the URL

echo "downloading images..."

# create the text file full of image URLs
# file first, then directory

images-file $DEST/temp-html $DEST/temp-url 

# wget the image URLs

old_IFS=$IFS
IFS=$'\n'
for line in $(cat $DEST/temp-url)
do
    wget -q -P $DEST $line
done
IFS=$old_IFS

echo "done."

# cleanup
rm $DEST/temp-html
rm $DEST/temp-url
