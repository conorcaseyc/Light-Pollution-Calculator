# Photopollution Calculator for Munster

> This program uses a mathematical model to predict photopollution based on population density for Munster, Ireland. 
> This work is part of [BT Young Scientist](https://btyoungscientist.com/) project, 'Is It Possible to Create a Mathematical Model to Predict Photopollution Based on Population Density in Munster'

## Usage

To run this program, you will need:

* [Python](https://www.python.org/) (2.7 or 3)
* [Pandas](https://pandas.pydata.org/) (can be installed with `pip install pandas`)

If you wish to use `data/solver.py` to develop the model, you will also need to install [Scipy](https://www.scipy.org/) and [Matplotlib](https://matplotlib.org/). 
This can be done with `pip install scipy matplotlib`.

This program can be used as a command line tool.
First, you will need to download the source code from github.

```bash
$ git clone https://github.com/conorcaseyc/Photopollution-Calculator
$ cd Photopollution-Calculator
```

Then you can run the program

```bash
$ python main.py
# alternatively, if you are using python3, you can run main_3.py
```

If you have any problems, please leave an issue.
For general feedback, please [email the developer](mailto:16ccasey@student.kenmarecs.com).

## Information

> Where did the population density for the towns come from?

They came from the Irish 2016 Census, and as a result are provided by the Central Statistics Office.

> Why does the program crash when I enter a town name into the program?

This is most likely due to the fact that you entered a town that is not included in the Central Statistics Office database for population density. There is also a probability you typed "license", "quit", or "help" into the section where you are asked to input a town name. These options can only be accessed when you are prompted "Is the name of the town being entered:".
  
> How do I open the files in the Map Data folder

All these files can be opened using a program called, QGIS (previously known as Quantum GIS). QGIS is a free and open-source cross-platform desktop geographic information system (GIS) program that supports viewing, editing, and analysis of geospatial data. This program can be downloaded from [qgis.org](https://qgis.org/en/site/forusers/download.html)
