#!/bin/bash
#SBATCH --job-name="dask-workers"
#SBATCH --output="dask-workers.%j.%N.out"
#SBATCH --partition=compute
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=24
#SBATCH --export=ALL
#SBATCH -t 0:20:00

module load singularity

SINGULARITY_IMAGE="/oasis/scratch/comet/zonca/temp_project/zonca-singularity-comet-master-2019-05.simg"
COMMAND="bash ./launch_worker.sh"
export SINGULARITY_BINDPATH="/oasis"

ibrun --npernode=1 singularity exec $SINGULARITY_IMAGE $COMMAND
