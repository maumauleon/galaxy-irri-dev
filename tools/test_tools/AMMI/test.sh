input=$1;

cp $input test.csv

report=$2;
expdes=$3;
biplotformat=$4;
plot3D=$5;
polygoner=$6;
analysis=$7;
LSMeans_par=$8;
traits=$9;
selected=$10; 

tmp=$RANDOM;

{

echo 'datos = read.csv("/home/dquoc/galaxy/tools/GEA-R/Yield_Data_for_CovENV.csv")'
echo 'ExpDes <- c("'$expdes'")'
echo 'BiplotFormat <- c("'$biplotformat'")'
echo 'plot3D <- '$plot3D''
echo 'polygoner <- '$polygoner''
echo 'analysis <- c("'$analysis'")'
echo 'LSMeans_par <- c("'$LSMeans_par'")'
echo 'traits <- c("'$traits'")'
echo 'tmp <- c("'$tmp'")'
echo 'selected <- c("'$selected'")'
echo 'source("/home/dquoc/galaxy/tools/GEA-R/AMMI&SREG.R")'

echo 'AMMISREG()'
} >run.R

Rscript ./run.R
dname='Output&'
mv $dname$tmp*/Final* $report

