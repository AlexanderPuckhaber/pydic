#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of pydic, a free digital correlation suite for computaing strain fields
#
# Author :  - Damien ANDRE, SPCTS/ENSIL-ENSCI, Limoges France
#             <damien.andre@unilim.fr>
#
# Copyright (C) 2017 Damien ANDRE
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http:#www.gnu.org/licenses/>.



# ====== INTRODUCTION
# The tensile example shows how to use the pydic module to compute
# the young's modulus and the poisson's ratio from picture captured
# during a tensile test. The loading were recorded during the test
# and the values are stored in the meta-data file (see 'img/meta-data.txt').
#
# Note that :
#  - pictures of the tensile test are located in the 'img' directory
#  - for a better undestanding, please refer to the 'description.png' file
#    that describes the tensile test 




# ====== IMPORTING MODULES
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
import os
import cv2

# locate the pydic module and import it
import imp
pydic = imp.load_source('pydic', '../../pydic.py')





#  ====== RUN PYDIC TO COMPUTE DISPLACEMENT AND STRAIN FIELDS
# read image series and write a separated result file 
pydic.init('./img/*.bmp', (80,80), (20,20), "/tmp/result.dic")

# and read the result file for computing strain and displacement field from the result file 
pydic.read_dic_file('/tmp/result.dic', interpolation='spline', save_image=True, scale_disp=10, scale_grid=25, meta_info_file='img/meta-data.txt')

# Now you can go in the 'img/pydic' directory to see the results :
# - the 'disp', 'grid' and 'marker' directories contain image files
# - the 'result' directory contain raw text csv file where displacement and strain fields are written  








# ======= STANDARD POST-TREATMENT : STRAIN FIELD MAP PLOTTING
last_grid = pydic.grid_list[-1]
last_grid.plot_field(last_grid.strain_xx, 'xx strain')
plt.show()






# ======== NON-STANDARD POST-TREATMENT : COMPUTE ELASTIC CONSTANTS (E & Nu)

# extract force from meta-data file 
force = np.array([float(x.meta_info['force(N)']) for x in pydic.grid_list])

# compute the maximal normal stress with this force
# the maximal normal stress is located in the lower plane 
L = (41-5)*1e-3 # see 'description.png' file 
l = (19-5)*1e-3 # see 'description.png' file
b = 7.66e-3    # see 'description.png' file
h = 4.06e-3    # see 'description.png' file
max_stress = (3./2.)* force *(L-l)/(b*h**2)


# now extract the maximal average strains on the lower plane of the sample along 
x_range = range(1                          , pydic.grid_list[0].size_x-1) 
y_range = range(pydic.grid_list[0].size_y-1, pydic.grid_list[0].size_y  )

# - use grid.average method to compute the average values of the xx and yy strains
max_strain_xx = np.array([grid.average(grid.strain_xx, x_range, y_range) for grid in pydic.grid_list])

# now compute Young's modulus thanks to scipy linear regression
E, intercept, r_value, p_value, std_err = stats.linregress(max_strain_xx, max_stress)

# and print results !
print "=> Young's modulus is E={:.2f} GPa".format(E*1e-9)


# enjoy !
# damien.andre@unilim.fr
