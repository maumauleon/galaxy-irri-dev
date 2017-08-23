#!/bin/bash

# The following block can be used by the job system
# to ensure this script is runnable before actually attempting
# to run it.
if [ -n "$ABC_TEST_JOB_SCRIPT_INTEGRITY_XYZ" ]; then
    exit 42
fi
Rscript --vanilla /home/galaxy/galaxy/tools/BGLR/bglr_wrapper.R  --csv_file '/home/galaxy/galaxy/database/files/000/dataset_62.dat'  --name_vector_column '1'  --data_vector_column '2'  --eta "/home/galaxy/galaxy/database/files/000/dataset_67.dat,BayesC"  --response_type 'gaussian'  --lower_bound_vector_column NULL  --upper_bound_vector_column NULL  --weights_vector_column NULL  --number_of_iterations '1500'  --burnin '500'  --thinning '5'  --saveat ""  --s0 NULL  --df0 '5.0'  --r2 '0.5'  --verbose 'TRUE'  --rmexistingfiles 'TRUE'  --groups_vector_column NULL  --nrandom '5' --p_out '5' --kfold NULL  --png_file_path /home/galaxy/galaxy/database/files/000/dataset_86.dat  --pdf_file_path /home/galaxy/galaxy/database/files/000/dataset_87.dat  --csv_file_path /home/galaxy/galaxy/database/files/000/dataset_88.dat