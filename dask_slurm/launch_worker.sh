echo "Launching dask worker"
# fix for ubuntu container
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
MEM_GB=100
# memory limit is in bytes
MEM=$(( $MEM_GB*1024**3 ))
/opt/conda/bin/dask-worker --scheduler-file ~/.dask_scheduler.json --memory-limit $MEM --nprocs 1
