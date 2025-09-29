# MACSS PZ Project

Materials for the photometric redshift (PZ) project in the MACSS.

## Lecture notes

You can find accompanying lecture notes [here](https://docs.google.com/presentation/d/1QsfjYt2fiOyNml7GlGNttCo2a4OBmEKFWw-qN9L57dI/edit?usp=sharing).


## Installation

These instructions assume that you already have a conda installation on your computer.

If you need to install conda, you can find instructions online, e.g., [here](https://www.anaconda.com/docs/getting-started/miniconda/install).

Open a terminal and do:

```bash
conda create -n macss -y python=3.12
conda activate macss
git clone https://github.com/KIPAC/MACSS.git
cd MACSS
pip install -e ".[dev]"
```


Test the installation and download the data for the examples:

```bash
py.test
```

This will download the data, create a directory in your home directory called `macss` and put the data there.


## Project Overview


This project is quite open-ended, but I'd like to at least see everyone:

1. explore both the Rubin catalog data (Part I)
2.  and the Reference data (Part II),
3. make a photometric redshift estimator and test it's properties on objects with known redshifts (Part III)

Time permitting, I encourage you to 

4. investigate a few ways you might improve the performance of the estimator (Part IV)
5. characterize how well the estimator does with imperfect data (Part V)
6. run your estimator on a sample of objects without known redshifts and estimate the redshift distribution of that sample (Part VI)

[More general information about the project](./intro.md)


### Part I: Catalog data exploration and preparation

Goals: explore the Rubin catalog data provided, and write some functions that will prepare catalog data for later analysis.

Specifics:  The rubin catalog data provides several different object fluxes, rather than magnitudes, and is does not account for the redenning cause by galactic dust.
You will need to:

1. investigate the contents of the Rubin object catalog,
2. convert fluxes and flux errors to magnitudes and magnitude errors,
3. account for galactic redenning,
4. convert from magnitudes to colors.

[More information about part 1 of the project](./part_1.md)


### Part 2: Reference data exploration 

Goals: explore the Rubin photometric reference data provided, and understand some of the details, such as the limiting depth, the photometric uncertainties.

Specifics: I have provided you with some prepared photometric reference data, which includes cross-matched objects with known redshifts.   You will want to:

1. investigate the contents of the Rubin photometric reference data,
2. understand the limitations of the data, such as the limiting depth, the incompleteness of the reference data sets, and the limited spatial resolution.

[More information about part 2 of the project](./part_2.md)



### Part 3: Creating and testing photometric redshift estimator

Goals: create a photometric redshift estimator using the scikit-learn tool-kit and test it out

Specifics: I have provided you with some prepared photometric reference data, which includes cross-matched objects with known redshifts.   You will want to:

1. prepare the data for consumption by the machine learning algorithms, 
2. use part of this data to train a regression model, 
3. apply that regression model to remainder of the data
4. investigate how well the regression model performed

[More information about part 3 of the project](./part_3.md)




### Part 4: Investigating ways to improve your regression model


Goals: investigate if you can improve your regression model using additional fluxes or morphology information 

Specifics: The data that I provided contain some additional information that might be useful in redshift estimation, such as the sizes of the galaxies, and the different flux measurements are sensitive to light from different parts of the galaxies.

You will need to:

1. look at correlations between various flux measurements and see if you can find additional information that might be useful,
2. try to add this information to a redshift estimation algorithm
3. look at correlations with additional morphology information such as the sizes of galaxies, and see if you can find additional information that might be useful,
4. try to add this morphology information to a redshift estimation algorithm.


[More information about part 4 of the project](./part_4.md)



### Part 5: Investigating how your regression model does with imperfect data

Goals: characterize how sensitive the model is to imperfect input data 

Specifics:  The test and training data is somewhat idealized, in that
we have selected galaxies that have well measured redshifts.  These
galaxies tend to be a brighter, and spatially isolated from other
galaxies.


You will need to:

1. artificially smear the photometric data to simulate photometric noise
2. artificially smear the photometric data to light contamination
   from nearby galaxies
3. see how these smearing affect the photometric redshift measurements.



[More information about part 5 of the project](./part_5.md)



### Part 6: Going from per-object estimates to ensemble estimates

Goals: go from per-object estimates to estimates of the distribution
of p(z) for an ensemble of objects. 

Specifics: Up to this point we have been worrying about the redshifts
of individual objects.  There are a lot of times what we care about is
actually the distribution of the redshifts of a great many objects.
We typically call these n(z) distributions, as opposed to per-object p(z).

You will want to: 

1. come up with a naive distribution of the n(z) for object in the
   test sample
2. apply the same methodology to a sample of object that we do not have reference redshifts for.
3. consider the systematic different between the test sample and the
   broader sample and how we might account for those.

[More information about part 6 of the project](./part_6.md)


[Page source](https://github.com/kipac/macss)

<!--  LocalWords:  macss scikit-learn
 -->
