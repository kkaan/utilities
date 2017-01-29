# -*- coding: utf-8 -*-
"""
Author Kankean Kandasamy

Sit in wait for files to be introduced to directory
Onnce new files are detected traverse through the images and convert them to 
mat files. 

MAT file stucture: 
<imagefilename>
tif array
"""
import os, os.path
import scipy.io as sio
import numpy
from PIL import Image

"""
import Tkinter as tk
import tkFileDialog as filedialog

root = tk.Tk()
root.withdraw()
dirname = filedialog.askdirectory()

tiffset = {}
"""


dirname = 'C:\Users\Kankean\Physics\MV\sample'

for f in os.listdir(dirname):
    ext = os.path.splitext(f)[1]
    if ext.lower() != '.tiff':
        continue
    im = Image.open(os.path.join(dirname,f))
    imarray = numpy.array(im)
    tiffset[f]=imarray

sio.savemat('test.mat', tiffset)




    




