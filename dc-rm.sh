#!/bin/bash
for i in `dcls $1`
do 
   echo $i
   dcdel $1/$i
done
dcrmdir $1
