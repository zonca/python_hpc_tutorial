# Webinar recording

https://www.sdsc.edu/Events/training/webinars/distributed_parallel_computing_with_python_2019/recording/

# Python for HPC

This webinar provides an introduction to distributed computing with Python, we will show how to modify a standard Python script to use multiple CPU cores using the concurrent.futures module from the Python standard library and then the dask package. Then we will leverage dask workers running on other machines to distribute a data processing task and monitor its execution through the live dask dashboard. You will understand the difference between threads and processes, how the Global Interpreter Lock works and principles of distributed computing. All material will be available as Jupyter Notebooks.

* `notebook_singularity.slrm`: SLURM script to launch a Jupyter Notebook job through Singularity
* `digits_of_pi/`: example of parallel programming estimating the digits of pi, using `concurrent.futures` and `dask`
* `dask` scripts: `launch_workers.sh` and `launch_scheduler.sh` and `dask_workers.slrm` launch all the components of `dask` `distributed`
* [Slides on Google Docs](https://docs.google.com/presentation/d/1hcgwy6S7QXVCIZHI0_Rb7_9FPHQP8HH6iWmaqCKpdIU/edit?usp=sharing)

