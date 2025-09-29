## Part I: Catalog data exploration and prepration

Goals: explore the Rubin catalog data provided, and write some functions that will prepare catalog data for later analysis.

If you have run the installation, you should have a directory called `macss/data` off you your home directory.  It contains some data we will be using.

Open the notebook `nb/Project_Part1.ipynb` to find a notebook you can work on this first part of the project in.


If you want to see what things should look like, you can have a look:

1. in the notebook [00_ExploreFluxes.ipynb](https://github.com/KIPAC/MACSS/blob/main/nb/00_ExploreFluxes.ipynb) to see examples of computing magnitudes and colors.


Specfics:  The Rubin catalog data provides several different object fluxes, rather than magnitudes, and is does not account for the redenning cause by galactic dust.
You will need to:

1. investigate the contents of the Rubin object catalog,
2. convert fluxes and flux errors to magnitudes and magnitude errors,
3. account for galacitic redenning,
4. convert from magnitudes to colors.


