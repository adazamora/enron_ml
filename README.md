# Machine Learning to analyze Enron data

I used supervised Machine Learning algorithms to predict persons of interest who might have been related to the fraud that led to the bankruptcy of Enron. Enron was a big "American energy, commodities, and services company" and on 2002 it was in bankruptcy due to fraud.

The data I used contained thousands of emails of the employees, financial information about Enron, and a list of "persons of interest", a hand generated list of people who were charged with crimes related to Enron, people who did not admit to be related to the fraud but paid fines and there were no criminal charges, and persons who testified in exchange for immunity from prosecution.

I did this project as part of the Intro to Machine Learning course, from the Data Analyst Nanodegree I took at Udacity.

## Requisites

To install the requirements on a Pyhon 2.7 conda environment:

```
conda install --file requirements.txt
```

To create a new environment that uses the requirements:

```
conda create --name <env> --file requirements.txt
```

## Files

I used a Jupyter notebook to do the data analysis and report my results. This file is called ml_project.

The functions I use in ml_project are in the following files:
- preliminar_analysis.py
- outliers_analysis.py
- new_features.py
- feature_selection.py
- ml_classifiers.py
 

## Data

The final_project_dataset.pkl contains the data I used in the project. The raw data can be found here: https://www.cs.cmu.edu/~enron/
