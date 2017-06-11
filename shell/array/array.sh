#!/bin/bash

totalnos=$#

echo "totalnos: ${totalnos}"
arrtotal=0

echo $1
for (( i=1; i<=${totalnos}; i++ ))
do
  echo "In put number is" $i
  arrtotal=`echo $i + ${arrtotal} | bc`
  echo "temp arry number is "$arrtotal
done

echo "Total of $@ = ${arrtotal}"
