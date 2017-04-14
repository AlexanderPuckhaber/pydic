# **pydic**, a python suite for local digital image correlation
![](https://gitlab.com/damien.andre/pydic/raw/master/doc/main-figure.png)


*pydic* is a free and easy-to-use python tool for digital image correlation (DIC). Note that *pydic* is not a 
graphical application. *pydic* is a python module, named `pydic.py`, deliver with 
didactic examples that may be used as tutorials. 

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
and [scipy](https://www.scipy.org/) are embedded in the main python packages 
such as [python(x,y)](https://python-xy.github.io/) or GNU/Linux distributions. Probably, you need 
to compile manually the [opencv2](http://opencv.org/) library. The installation and compilation procedure of opencv2 is 
detailed in the [official tutorial page about opencv2](http://docs.opencv.org/2.4/doc/tutorials/introduction/table_of_content_introduction/table_of_content_introduction.html#table-of-content-introduction). Once you have done this work, you can 
download the *pydic* package and go to the `examples` directory to run the *tensile test* or the *four point bending test* examples.


# Running the four point bending test example
Go to the `examples/4-pt-bending-test` and simply run with python the `main.py` file. This `main.py` file 
shows how to use *pydic* for :
1. read the `*.dic` and compute (and eventually smooth) displacement and strain fields with `pydic.read_dic_file()` method. This step write a series of results files. These files are located in the `img` folder where :
2. open an image list, compute the displacement for each image and write the results in a `*.dic` file with the `pydic.init()` method
 * the `disp` folder contains pictures that paint the displacement field
 * the `grid` folder contains pictures that paint the displacement grid
 * the `marker` folder contains pictures the displacement of the correlated windows
 * the `result` folder contains [csv](https://en.wikipedia.org/wiki/Comma-separated_values) result files. These files 
 can be used to post-treat the results with your favorite tool such as spreadsheet softwares. #You can go at the bottom of this 
 to get an overview of these images.#
 3. plotting strain field interactive maps thanks to matplotlib
 4. using meta-data file to store sensor data for each picture such as the loading force
 5. using the power of the python language to make complex post-treatment such as automatically computing the Young's modulus from 
 strain fields and meta-data.K information.
 
# Quick overview of result image files : *disp*, *grid* and *marker* files
The following animated gif shows the results of a series of `disp` images where the displacement are painted by red lines 
and scaled by a 10x factor. 
![](https://gitlab.com/damien.andre/pydic/raw/master/doc/disp.gif)

The following animated gif shows the results of a series of `grid` images where the grid strain is scaled by a 25x factor. 
![](https://gitlab.com/damien.andre/pydic/raw/master/doc/grid.gif)

Finally, the following animated gif shows the displacement of markers that correspond to the center of correlation windows.
![](https://gitlab.com/damien.andre/pydic/raw/master/doc/marker.gif)

In addition, the *four point bending test example* shows how to :
 * plot strain field interactive map
 * use meta-data file that can store meta-information for each picture 
 * benefits of the power of the python language to make complex post-treatment such as automatically computing the Young's modulus from the computed strain field and the meta-data information.
