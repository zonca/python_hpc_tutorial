Advanced Pandas topics with an example in Astrophysics
======================================================

In this example we will work with observations of the Cosmic Microwave Background from the [Planck satellite](https://en.wikipedia.org/wiki/Planck_(spacecraft)) using advanced functionalities of `pandas` and `numpy` and we will create plots with `matplotlib`.

In section 1 we will read a map created by the Planck satellite and we will familiarize with HDF5 format and working with hierarchical indexing in `pandas`. We will also visualize sky maps in `matplotlib` using a curvilinear projection.

In section 2 we will use `numpy` to create a simulation of how Planck scans the sky thoughout a year of observations and we will plot scanning rings in different reference frames. We will also create a interactive widget with `ipywidgets`.

In section 3 we will use the scanning coordinates created in section 2 to simulate an observation of the map used in setion 1. We will add white noise and then learn how to use `pandas` groupby with hierarchical index to aggregate the data into a sky map. We will finally compare the simulated noisy map with the original map and study its features.

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
