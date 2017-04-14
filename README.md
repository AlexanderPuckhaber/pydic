# pydic, a python suite for digital image correlation
![dqsdqsdqs](https://gitlab.com/damien.andre/pydic/blob/master/doc/logo.png)


*pydic* is a free and easy-to-use python tool for digital image correlation (DIC). *pydic* is not a 
graphical application , pydic is a python module named `pydic.py` deliver with a set of 
didactic examples.


From a set of pictures, *pydic* can compute the displacement and the strain fields 
inside a zone of interest. If you want to learn more about digital image correlation,
you can visit the [wikipedia page](https://en.wikipedia.org/wiki/Digital_image_correlation).

Note that the method used here is said as *local* digital image correlation. The main problem
with the local digital image correlation is the induced noise. *pydic* embeds 
a set of numerical tools for reducing this noise and computing smoothed strain fields. 

Another interesting feature of *pydic* is the capability to compute displacement and strain fields 
from a non-grid-aligned set of points. This feature may be useful to optimize the digital 
image correlation and let automatic choosing best points for DIC thanks to algorithm such as the [goodFeaturesToTrack](http://docs.opencv.org/2.4.8/modules/imgproc/doc/feature_detection.html) from the [opencv](http://docs.opencv.org/2.4/) library.

# Installation
*pydic* is based on [matplotlib](https://matplotlib.org/), [numpy](http://www.numpy.org/), 
[scipy](https://www.scipy.org/) and [opencv2](http://opencv.org/). You have to install
these libraries to use *pydic*. Generally, [matplotlib](https://matplotlib.org/), [numpy](http://www.numpy.org/), 
and [scipy](https://www.scipy.org/) are embedded in the main python distribution 
such as [python(x,y)](https://python-xy.github.io/) or GNU/Linux distributions. Probably, you need 
to compile manually the [opencv2](http://opencv.org/) library. The installation and compilation procedure of opencv2 is 
detailed in the [official tutorial page about opencv2](http://docs.opencv.org/2.4/doc/tutorials/introduction/table_of_content_introduction/table_of_content_introduction.html#table-of-content-introduction). Once you have done this work, you can 
go to the `examples` directory to run *tensile test* or *four point bending test* examples.


