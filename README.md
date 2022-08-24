# Semantic Change and Analysis of Hansard Data

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

The Project does the analysis on the hansard data of the UK HOC parliamentary speeches. 
> We would analyze the data and look for semantic change in the context in parliamentary speeches, topic modelling via existing and naive methods, along with the co-occurence network in the speeches.

## Installation

Project requires [Anaconda](https://nodejs.org/) to run with python 3.9

Create a virtual env in conda and install the dependencies

### Model download 

From the website https://zenodo.org/record/2597441#.YvtzdHbMKUk  download Cr5 model(joint_28_en.txt.gz) and place it under folder ./model/Cr5-master

```sh
conda create -n<env_name> python==3.9 -y
pip install -r requirements.txt
```

## Running the Code

Execute the file
```sh
main.ipynb
Rull all code
```

## Running the Plotly Dash Server

Execute the file
```sh
python hoc.py
```

