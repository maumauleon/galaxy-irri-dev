input=$1;

cp $input test.csv


report=$2;
expdes=$3;
analysis=$4;
LSMeans_par=$5;
traits=$6;
selected=$7; 
gbtest=$8;
pc12=$9;
pc23=${10};
pc13=${11};
pctr=${12};
html=${13};
tmp=$RANDOM;

{

echo 'datos = read.csv("test.csv")'
echo 'ExpDes <- c("'$expdes'")'
echo 'BiplotFormat <- c("pdf")'
echo 'plot3D <- c("TRUE")'
echo 'polygoner <- c("TRUE")'
echo 'analysis <- c("'$analysis'")'
echo 'LSMeans_par <- c("'$LSMeans_par'")'
echo 'traits <- c("'$traits'")'
echo 'tmp <- c("'$tmp'")'
echo 'selected <- c("'$selected'")'
echo 'source("AMMI&SREG.R")'

echo 'AMMISREG()'
} >run.R

Rscript run.R
dname='Output&'
mv $dname$tmp*/Final* $report
mv $dname$tmp*/Gollob* $gbtest
mv $dname$tmp*/*PC1*PC2* $pc12
mv $dname$tmp*/*PC2*PC3* $pc23
mv $dname$tmp*/*PC1*PC3* $pc13
mv $dname$tmp*/PC1*Trait* $pctr
mv $dname$tmp*/*.html $html

