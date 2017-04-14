# pydic, a python suite for digital image correlation
pydic is a free and easy-to-use python tool for digital image correlation. 
From a set of pictures, pydic can compute the displacement and the strain fields 
inside a zone of interest. If you want to learn more about digital image correlation,
you can visit the [wikipedia page](https://en.wikipedia.org/wiki/Digital_image_correlation).

Note that the method used here is said as *local* digital image correlation. The main problem
with the local digital image correlation is the noise induced by a lot of factors. pydic embeds 
some numerical tools to reduce this noise and compute smoothed strain fields. Another feature of pydic
is the capability to compute displacement and strain fields from a non-grid-aligned set of 
points. This feature may be useful to optimize the digital image correlation and let automatic 
choosing best points for dic thanks to algorithm such as the [goodFeaturesToTrack](http://docs.opencv.org/2.4.8/modules/imgproc/doc/feature_detection.html) from the [opencv](http://docs.opencv.org/2.4/) library.


pydic is an easy-to-use python module for computing strain field maps 
from a serie of pictures.

pydic depends on matplotlib, numpy, scipy and opencv2. You have 
to install them before running pydic. 

After these installation you can go to the examples directory to
get a quick overview of the pydic features.

[I link to the Milestones page](./doc/README.md)
