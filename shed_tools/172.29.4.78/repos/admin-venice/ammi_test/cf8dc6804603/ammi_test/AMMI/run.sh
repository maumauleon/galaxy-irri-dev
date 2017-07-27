#!/bin/bash

input=$1;
expdes=$2;
biplotformat=$3;
plot3D=$4;
polygoner=$5;
analysis=$6;
LSMeans_par=$7;
traits=$8;
selected=$9;

{

echo 'datos = read.csv("'$input'")'
echo 'ExpDes <- c("'$expdes'")'
echo 'BiplotFormat <- c("'$biplotformat'")'
echo 'plot3D <- '$plot3D''
echo 'polygoner <- '$polygoner''
echo 'analysis <- c("'$analysis'")'
echo 'LSMeans_par <- c("'$LSMeans_par'")'
echo 'traits <- c("'$traits'")'

echo 'selected <- c("'$selected'")'
echo 'source("AMMI&SREG.R")'

echo 'AMMISREG()'
} >run.R

Rscript ./run.R