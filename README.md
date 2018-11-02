# Python for HPC

**The `UCSDGUEST` wireless network blocks all non-standard ports**

Therefore please use `UCSD-PROTECTED` or `eduroam` if you can,
otherwise we will setup another wireless network with a different name.


* `notebook_singularity.slrm`: SLURM script to launch a Jupyter Notebook job through Singularity
* `digits_of_pi/`: example of parallel programming estimating the digits of pi, using `concurrent.futures` and `dask`
* `dask` scripts: `launch_workers.sh` and `launch_scheduler.sh` and `dask_workers.slrm` launch all the components of `dask` `distributed`
* Slides are not complete, see `notes.md`
