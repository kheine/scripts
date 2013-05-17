#!/bin/bash
mkdir $2
for i in `dcls "$1" | grep root`
do
   echo $i
   echo "cp $1/$i $2/$i"
   dcget $1/$i $2/$i
done

