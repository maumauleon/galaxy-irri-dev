#!/bin/bash

input=$1

#cp $input test.csv
tmp=$RANDOM
cp $input $tmp".csv"

#report=$2;
#expdes=$3;
#analysis=$4;
#LSMeans_par=$5;
#traits=$6;
#selected=$7; 
#gbtest=$8;
#pc12=$9;
#pc23=${10};
#pc13=${11};
#pctr=${12};
#html=${13};
#tmp=$RANDOM;

Rscript AMMI_SREG2.R $input $2 $3 $4 $5 $6 $7 $8 $9 $tmp
#mv $tmp/Final* $report
#mv $tmp/Gollob* $gbtest
#mv $tmp/*PC1*PC2* $pc12
#mv $tmp/*PC2*PC3* $pc23
#mv $tmp/*PC1*PC3* $pc13
#mv $tmp/PC1*Trait* $pctr
#mv $tmp/*.html $html
#rm $tmp".csv"
echo $tmp
