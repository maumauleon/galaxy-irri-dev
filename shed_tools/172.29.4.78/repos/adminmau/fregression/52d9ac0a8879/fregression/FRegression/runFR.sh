input=$1;
cp $input input.csv
cov=$2;
cp $cov cov.csv
expdes=$3;
traits=$4;
typecov=$5;
selected=$6;
cpv=$7
report=$8;
tmp=$RANDOM

{

echo 'datos = read.csv("input.csv")'
echo 'file_nameCOV = read.csv("cov.csv")'
echo 'ExpDes <- c("'$expdes'")'
echo 'cpv <- c('"$cpv"')'
echo 'traits <- c("'$traits'")'
echo 'typecov <- c("'$typecov'")'
echo 'tmp <- c("'$tmp'")'
echo 'selected <- c("'$selected'")'
echo 'source("/home/dquoc/galaxy/tools/GEA-R/FRegression/FactorialRegression.R")'

echo 'REGFACT()'
} >run.R

Rscript ./run.R
dname='Output'
mv $dname*$tmp*/Result*  $report








