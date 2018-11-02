## Introduction

What it is? 

A command line text only interface to filesystem (like file manager GUI) + execute commands on files (like double clicking or open with menu in file manager GUI)

Ask students not to take notes and show quickly that `ls` is same as file manager GUI, `mkdir` creates a folder that shows up in the file manager GUI, show `cd` in and out a folder.

The purpose here is to show students that never saw a command line interface before what it is.

* Motivation: ssh into a supercomputer, bash is the only interface available
* Motivation: automate everything, let the computer do boring stuff

## Motivating exercise

We have a tar archive with some data files and some badly formatted files,
we want to learn how to:

* Delete some useless files
* Rename the good files with a better name
* Apply an analysis script that works on 1 file a time to all data files
* Move plots and output `.csv` in separate folders
* Put this in a bash script so we can automate the process next time we get a data delivery

## First bash commands

* `pwd` print out current folder
* `ls` lists files in current folder
* `ls targetfolder` lists files in target folder (use only relative paths)
* `ls -F` identifies folders with /
* `cd foldername` changes directory to foldername
* `cd` changes directory to home folder
* `ls ..` lists files in parent folder
* `echo Hello World` print a string

## Shell expansion

It is important students understand that it is performed by the shell, not by the commands,
common misconception is:

`ls *.csv` `ls` filters the files that ends with `csv`.
Wrong! It is the shell that sends to `ls` the list of files that ends with `csv` separated by spaces.

Better only use `*`, unless they ask, then show `?`.

So, don't start with `ls` but just with `echo`:

* `cd` to folder that has `csv` files
* `echo "*csv"` this prints the string `*csv`
* `echo *csv` try this on your machine, what happens? 
* `ls *.csv` here `ls` gets already the list of `csv` files

## Get the archive, unzip and remove bad files

Back to the exercise, get the data zip file using `curl`:

```bash
curl https://github.com/zonca/swcarpentry-workshop-pandas/blob/master/rawdata/rawdata.zip?raw=true -o rawdata.zip -L
```

The first parameters is the URL of the file, `-o` specifies the name of the output file, and `-L` is necessary to follow the redirects on Github, this is generally not necessary on other websites.

We can now remove the useless files (first always use `ls` or `echo`):

`ls / rm _*.csv`

## Batch files renaming

The data files have extension `.txt`, actually `.csv` is more descriptive,
so we want to rename all of them in batch mode:

Rename files using:

    for f in *.txt
    do 
        mv $f ${f/txt/csv}
    done

* `${f/txt/csv}` replaces every occurrence of `txt` with `csv`
* `for` is repeating the `mv` operation for every `csv` file.

## Run analysis script

Go quickly through the script, show that the script works with just 1 file,
opens it, plots it and saveas a `png` or `pdf`.

Now use bash to run this on all files:

    for f in *.csv
    do
        ~/anaconda/Scripts/ipython.exe analyze_mosquito_script.py $f
    done

Check that all the figures were created.

Move figures to subfolder:

    mkdir figures_png
    mv *png figures_png/

## Show integrated bash script

The purpose is to run all our analysis pipeline with a single command,
this is a bash script that does data cleaning and then launches our Python script
on every input data file.

See the final version of the `pipeline.sh` script: 

* <https://github.com/zonca/software-carpentry-workshop/blob/master/pipeline.sh>
