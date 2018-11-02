echo "Launching dask scheduler"
# fix for ubuntu container
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
dask-scheduler --scheduler-file ~/.dask_scheduler.json --host $(hostname)
