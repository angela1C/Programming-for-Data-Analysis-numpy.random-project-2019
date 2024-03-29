This repository contains my submission for the Programming for Data Analysis Module 2019 Practical Assignment for the Programming for Data Analysis at GMIT as part of the Higher Diploma in Computing and Data Analytics.



# Problem Statement.

The assignment concerns the **numpy.random** package in Python. We are required to create a Jupyter notebook explaining the use of the package, including detailed explanations of at least five of the distributions provided for in the package. There are four distinct tasks to be carried out in your Jupyter notebook.

1. Explain the overall purpose of the package.
2. Explain the use of the “Simple random data” and “Permutations” functions.
3. Explain the use and purpose of at least five “Distributions” functions
4. Explain the use of seeds in generating pseudorandom numbers.

The required documents for the assignment submission are in this git repository and include:

- This README.md file
- a git ignore file
- a Jupyter Notebook

The instructions for this assignment is also available in this repository called **Practical_Assignment_Instructions**


## How to download this repository

Go to the URL for the repository on GitHub at https://github.com/angela1C/numpy.random
Click the green Clone or download button

## How to run the code

**Python 3** was used to develop this project. Python 3 can be downloaded from the official Python website at https://www.python.org/downloads/. It can also be downloaded using the **Anaconda Python distribution** at https://www.anaconda.com/distribution/

However, the Jupyter Notebook [NumpyRandom.ipynb](https://github.com/angela1C/numpy.random/blob/master/NumpyRandom.ipynb) with all it's code and output can be viewed directly in this GitHub repository in the browser without Python 3 installed.

If, however the notebook doesn't render on GitHub as may happen from time to time, the url for this repository https://github.com/angela1C/numpy.random can be copied and pasted into the [Jupyter nbviewer ](https://nbviewer.jupyter.org ) at
https://nbviewer.jupyter.org  where you enter the location of a Jupyter Notebook and click `Go` to have it rendered there.

The aim of the project is to look at the numpy.random package and to be able to describe it in our own words.

I started this project by first getting familiar with the [Python NumPy](https://numpy.org/doc/1.16/reference/index.html#numpy-reference) reference manual and the [NumPy Quickstart tutorial](https://numpy.org/doc/1.16/user/quickstart.html) in the [NumPy User Guide](https://numpy.org/doc/1.16/user/index.html#numpy-user-guide) before looking at the [Random sampling (numpy.random)](https://numpy.org/doc/1.16/reference/routines.random.html) listed under the numpy routines of the user guide.

Version 1.16.2 is the version of NumPy that I am working with on my machine, therefore the documentation I am referring to in the notebook is the [NumPy Reference 1.16](https://numpy.org/doc/1.16/reference/index.html#numpy-reference) manual. 

This reference manual details functions, modules, and objects included in NumPy, describing what they are and what they do. It contains detailed reference documentation of the functions and classes contained in the NumPy package. 

I then went through the four main sections of the NumPy Random module looking at the [simple random data](https://numpy.org/doc/1.16/reference/routines.random.html#simple-random-data) and [permutation](https://numpy.org/doc/1.16/reference/routines.random.html#permutations) functions, before looking at the [distribution](https://numpy.org/doc/1.16/reference/routines.random.html#distributions) functions and the [Random Generator](https://numpy.org/doc/1.16/reference/routines.random.html#random-generator) section to get an idea of the numpy.random module. 
I referred to many online resources such as blogs and these are noted in the references section. 
I found that there seemed to be some functions that appeared to do similar things and often the reference manual for one function referred to an example of a similar function with a different name.

The **simple random data** functions all had related **distribution** functions. Therefore any plots are shown in the section describing the **distribution**  functions to avoid duplications. 

The notebook is laid out as follows:

- [Python tools used for this assignment](#tools)
- [Task 1: Explain the overall purpose of the package](#task1)
- [Task 2: Explain the use of the Simple random data and Permutations functions.](#task2)
    - [Simple random data functions](#task2.1)
    - [Permutations Functions](#task2.2)
- [Task 3: Explain the use and purpose of at least five “Distributions” functions](#task3)
- [Task 4: Explain the use of seeds in generating pseudorandom numbers](#task4)
- [References](#references)
  
