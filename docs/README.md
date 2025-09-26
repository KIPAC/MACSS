# MACSS PZ Proejct

Materials for the photometric redshift (PZ) project in the MACSS.


## Installation

These instructions assume that you already have a conda installation on your computer.

```bash
conda create -n macss python=3.12
git clone https://github.com/KIPAC/MACSS.git
cd MACSS
pip install -e ".[dev]"
```


Test the installation and download the data for the exampes

```bash
py.test
```

This will download the data, create a directory in your home directory called `macss` and put the data there.


## Project Overview


This project is quite open-ended, but I'd like to at least see everyone:

1. explore both the Rubin catalog data (Part I) and the Reference data (Part II),
2. make a photometric redshift estimator and test it's properties on objects with known redshifts (Part III)

Time permitting, I encourage you to 

3. investigate a few ways you might improve the preformance of the estimator (Part IV)
4. characterize how well the estimator does with imperfect data (Part V)
5. run your estimator on a sample of objects without known redshifts and estimate the redshift distribution of that sample (Part VI)


### Part I: Catalog data exploration and prepration

Goals: explore the Rubin catalog data provided, and write some functions that will prepare catalog data for later analysis.

Specfics:  The rubin catalog data provides several different object fluxes, rather than magnitudes, and is does not account for the redenning cause by galactic dust.
You will need to:

1. investigate the contents of the Rubin object catalog,
2. convert fluxes and flux errors to magnitudes and magnitude errors,
3. account for galacitic redenning,
4. convert from magnitudes to colors.


### Part 2: Reference data exploration, 

Goals: explore the Rubin photometric reference data provided, and understand some of the details, such as the limiting depth, the photo-metric uncertainties

Specfics: I have provided you with some prepared photometric reference data, which includes cross-matched objects with known redshifts.   You will want to:

1. investigate the contents of the Rubin photometric reference data,
2. understand the limitations of the data, such as the limiting depth, the incompletness of the reference data sets, and the limited spatial resolution.


### Part 3: Creating and testing photometric redshift estimator

Goals: create a photometric redshift estimator using the scikit-learn tool-kit and test it out

Specfics: I have provided you with some prepared photometric reference data, which includes cross-matched objects with known redshifts.   You will want to:

1. perpare the data for consumption by the machine learning algorithms, 
2. use part of this data to train a regression model, 
3. apply that regression model to remainder of the data
4. investiage how well the regresion model performed


### Part 4: Investigating ways to improve your regression model

Goals: investigate if you can improve your regression model using additional fluxes or morphology information 

Specfics: 


### Part 5: Investigating how your regression model does with imperfect data

Goals: characterize how senstive the model is to imperfect input data 

Specfics: 








[Page source](https://github.com/kipac/macss)
