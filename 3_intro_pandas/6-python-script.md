# Command line programs in Python (aka Python scripts)

## Creating a Python script

The IPython Notebook and other interactive tools are great for prototyping code and exploring data, but sooner or later we will want to use our program in a pipeline or run it in a shell script to process thousands of data files. In order to do that, we need to make our programs work like other Unix command-line tools. For example, we may want a program that reads a data set, performs the fit and saves both the plot and the output fit parameters to files.

First of all, let's create another `.py` file named `analyze_mosquito_data_script.py` in our repository folder 
and let's copy the code we used in the last class on Python to run the functions defined in `analyze_mosquito_data_lib.py` on our data.

```python
    import pandas as pd
    import analyze_mosquito_data_lib as mosquito_lib
    
    filename = "A1_mosquito_data.csv"
    data = pd.read_csv(filename)
    parameters = mosquito_lib.analyze(data)
    print(parameters)
```

Now we can run this script in batch mode from the command line, without opening the IPython notebook on Linux and Mac as:

    ~/anaconda/bin/python analyze_mosquito_data_script.py

or (on Windows):

    ~/Anaconda/Scripts/ipython.exe analyze_mosquito_data_script.py

Python runs this script line by line, somehow similarly to running every cell of an IPython Notebook with the "Run All" button.

What is the difference between a module and a script?

* `analyze_mosquito_data_lib.py` is a module, it is a library that just defines functions, it doesn't actually run any analysis, it is a library that collects functions we can re-use in any number of IPython Notebooks or scripts.
* `analyze_mosquito_data_script.py` is a script, it imports the functions defined in different libraries and executes them to actually run an analysis and produce results.

We want to try keep a script as simple as possible, all of our algorithms should be implemented in a library,
so that they can be re-used, shared and improved over time. Generally the library is what is published online on Github, generally together with some sample scripts to show how to use the library.

## Saving output files

The script only prints the output parameters to the console,
first thing we need to implement saving the parameters to file and saving the plot to disk.

The `parameters` variable is a data structure defined in `pandas` and has a method to write its own content
to disk as comma separated values, `.to_csv`:

```python
parameters.to_csv("parameters.csv")
```

Saving a plot is accomplished calling:
   
```python
plt.savefig("output_plot.png")
```

just after `plt.plot` in the `analyze` function of `analyze_mosquito_data_lib.py`, where the extension of the file can be `.jpg`, `.png`, `.pdf` and many more.

## Dynamic output filenames

If we modify the `filename` variable in the script, we can run the analysis on other files, however the output plot and `.csv` would be overwritten because they have the same name.

We need to dynamically create the name of the output files.
First of all the `analyze` function needs to get the output figure filename as an input parameter, because at function definition we have no knowledge of what will be the name of the output file.

The final version of the function will be:

```python
def analyze(data, figure_filename):
    plt.savefig(figure_filename)

```

If the input `filename` is `A1_mosquito_data.csv`, we could like the outputs to be `A1_mosquito_data.png` `A1_mosquito_parameters.csv`.
We can achieve this with the `replace` method of the `filename` string:

```python
filename.replace("csv", "png").replace("data", "plot_" + variable)
filename.replace("data", "parameters_" + variable)
```

Therefore the current version of `analyze_mosquito_data_script.py` is:

```python
    import pandas as pd
    import analyze_mosquito_data_lib as mosquito_lib
    
    filename = "A1_mosquito_data.csv"
    data = pd.read_csv(filename)
    mosquito_lib.analyze(data, filename)
```

## Arguments from the command line

Finally we would like to be able to call this script from the command line and choose the target file as:

    python analyze_mosquito_data_script.py B1_mosquito_data.csv
    
Python support this via the `sys` standard library module:

    import sys
    filename = sys.argv[1]

`sys.argv` is a list of strings, the zeroth element is the name of the actual script, then all the other elements are the other arguments.

The final version of the script is:

```python
import sys
import pandas as pd
import analyze_mosquito_data_lib as mosquito_lib

filename = sys.argv[1]

print "Analyzing", filename

# read the data
data = pd.read_csv(filename)
							  
print "Running analyze"
mosquito_lib.analyze(data, filename)
```
