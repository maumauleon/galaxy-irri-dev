#!/bin/bash



# The following block can be used by the job system
# to ensure this script is runnable before actually attempting
# to run it.
if [ -n "$ABC_TEST_JOB_SCRIPT_INTEGRITY_XYZ" ]; then
    exit 42
fi

GALAXY_SLOTS="1"; export GALAXY_SLOTS;
export GALAXY_SLOTS
PRESERVE_GALAXY_ENVIRONMENT="False"
GALAXY_LIB="/home/galaxy/galaxy/lib"
if [ "$GALAXY_LIB" != "None" -a "$PRESERVE_GALAXY_ENVIRONMENT" = "True" ]; then
    if [ -n "$PYTHONPATH" ]; then
        PYTHONPATH="$GALAXY_LIB:$PYTHONPATH"
    else
        PYTHONPATH="$GALAXY_LIB"
    fi
    export PYTHONPATH
fi

GALAXY_VIRTUAL_ENV="/home/galaxy/galaxy/.venv"
if [ "$GALAXY_VIRTUAL_ENV" != "None" -a -z "$VIRTUAL_ENV" \
     -a -f "$GALAXY_VIRTUAL_ENV/bin/activate" -a "$PRESERVE_GALAXY_ENVIRONMENT" = "True" ]; then
    . "$GALAXY_VIRTUAL_ENV/bin/activate"
fi
echo "$GALAXY_SLOTS" > '/home/galaxy/galaxy/database/jobs_directory/000/21/__instrument_core_galaxy_slots' 
date +"%s" > /home/galaxy/galaxy/database/jobs_directory/000/21/__instrument_core_epoch_start
cd /home/galaxy/galaxy/database/jobs_directory/000/21
rm -rf working; mkdir -p working; cd working; /home/galaxy/galaxy/database/jobs_directory/000/21/tool_script.sh; return_code=$?; cd '/home/galaxy/galaxy/database/jobs_directory/000/21'; 
if [ "$GALAXY_LIB" != "None" ]; then
    if [ -n "$PYTHONPATH" ]; then
        PYTHONPATH="$GALAXY_LIB:$PYTHONPATH"
    else
        PYTHONPATH="$GALAXY_LIB"
    fi
    export PYTHONPATH
fi
if [ "$GALAXY_VIRTUAL_ENV" != "None" -a -z "$VIRTUAL_ENV"      -a -f "$GALAXY_VIRTUAL_ENV/bin/activate" ]; then
    . "$GALAXY_VIRTUAL_ENV/bin/activate"
fi
GALAXY_PYTHON=`command -v python`
python "/home/galaxy/galaxy/database/jobs_directory/000/21/set_metadata_pBS3kq.py" "/home/galaxy/galaxy/database/tmp/tmpFsp7mB" "/home/galaxy/galaxy/database/jobs_directory/000/21/working/galaxy.json" "/home/galaxy/galaxy/database/jobs_directory/000/21/metadata_in_HistoryDatasetAssociation_86_WOvwEH,/home/galaxy/galaxy/database/jobs_directory/000/21/metadata_kwds_HistoryDatasetAssociation_86_8KLw0C,/home/galaxy/galaxy/database/jobs_directory/000/21/metadata_out_HistoryDatasetAssociation_86_FBHTV7,/home/galaxy/galaxy/database/jobs_directory/000/21/metadata_results_HistoryDatasetAssociation_86_aM6FdY,/home/galaxy/galaxy/database/files/000/dataset_86.dat,/home/galaxy/galaxy/database/jobs_directory/000/21/metadata_override_HistoryDatasetAssociation_86_caN121" "/home/galaxy/galaxy/database/jobs_directory/000/21/metadata_in_HistoryDatasetAssociation_87_NgfIdV,/home/galaxy/galaxy/database/jobs_directory/000/21/metadata_kwds_HistoryDatasetAssociation_87_EIbSuy,/home/galaxy/galaxy/database/jobs_directory/000/21/metadata_out_HistoryDatasetAssociation_87_KDkWqD,/home/galaxy/galaxy/database/jobs_directory/000/21/metadata_results_HistoryDatasetAssociation_87_eiISU7,/home/galaxy/galaxy/database/files/000/dataset_87.dat,/home/galaxy/galaxy/database/jobs_directory/000/21/metadata_override_HistoryDatasetAssociation_87_HwsZB3" "/home/galaxy/galaxy/database/jobs_directory/000/21/metadata_in_HistoryDatasetAssociation_88_7eQXy7,/home/galaxy/galaxy/database/jobs_directory/000/21/metadata_kwds_HistoryDatasetAssociation_88_Mr825p,/home/galaxy/galaxy/database/jobs_directory/000/21/metadata_out_HistoryDatasetAssociation_88_ZUDptR,/home/galaxy/galaxy/database/jobs_directory/000/21/metadata_results_HistoryDatasetAssociation_88_Wki9kO,/home/galaxy/galaxy/database/files/000/dataset_88.dat,/home/galaxy/galaxy/database/jobs_directory/000/21/metadata_override_HistoryDatasetAssociation_88_sfCHi_" 5242880; sh -c "exit $return_code"
echo $? > /home/galaxy/galaxy/database/jobs_directory/000/21/galaxy_21.ec
date +"%s" > /home/galaxy/galaxy/database/jobs_directory/000/21/__instrument_core_epoch_end
