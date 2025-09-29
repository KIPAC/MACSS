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



If you want to see what things should look like, you can have a look:

1. in the notebook [Extra_NoiseStudy.ipynb](https://github.com/KIPAC/MACSS/blob/main/nb/Extra_NoiseStudy.ipynb) to see examples adding random photometric noise and seeing how it affects the p(z) estimation.

2. in the notebook [Extra_AdmixStudy.ipynb](https://github.com/KIPAC/MACSS/blob/main/nb/Extra_AdmixStudy.ipynb) to see examples adding contamination from other galaxies and seeing how it affects the p(z) estimation. 







<!--  LocalWords:  Extra_NoiseStudy.ipynb Extra_AdmixStudy.ipynb
 -->
