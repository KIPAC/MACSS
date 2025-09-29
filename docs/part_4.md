### Part 4: Investigating ways to improve your regression model

Goals: investigate if you can improve your regression model using additional fluxes or morphology information 

Specifics: The data that I provided contain some additional information that might be useful in redshift estimation, such as the sizes of the galaxies, and the different flux measurements are sensitive to light from different parts of the galaxies.

You will need to:

1. look at correlations between various flux measurements and see if you can find additional information that might be useful,
2. try to add this information to a redshift estimation algorithm
3. look at correlations with additional morphology information such as the sizes of galaxies, and see if you can find additional information that might be useful,
4. try to add this morphology information to a redshift estimation algorithm.



If you want to see what things should look like, you can have a look:

1. in the notebook [07_GalaxySize.ipynb](https://github.com/KIPAC/MACSS/blob/main/nb/07_GalaxySize.ipynb) to see examples of computing magnitudes and colors.

2. in the notebook [08_Morphology.ipynb](https://github.com/KIPAC/MACSS/blob/main/nb/08_Morphology.ipynb) to see some studies of how the different flux measurement are affected by the Galaxy size, and how that correlates with redshift.

3. in the notebook [09_CosmoSize.ipynb](https://github.com/KIPAC/MACSS/blob/main/nb/09_CosmoSize.ipynb) to see how a Milkyway like Galaxy might appear at different redshifts.

4. in the notebook [10_SklearnMorphology.ipynb](https://github.com/KIPAC/MACSS/blob/main/nb/10_SklearnMorphology.ipynb) to see an example of adding some morphology information to a redshift estimation algorithm.








<!--  LocalWords:  07_GalaxySize.ipynb 08_Morphology.ipynb
 -->
<!--  LocalWords:  09_CosmoSize.ipynb 10_SklearnMorphology.ipynb
 -->
