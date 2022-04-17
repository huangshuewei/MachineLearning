# -*- coding: utf-8 -*-
"""
Example of loading images from files
"""


import numpy as np
from scipy import misc,ndimage
import matplotlib.pyplot as plt
from skimage import io,color
import os

face_im = io.imread('tfc_face_01.jpg')

# Or to use the full path
#face_im = io.imread(r"C:\Users\mddbstfc\LocalWindowsData\Lectures\MedImMSc2018\MedImAn+MathsComp\L5_Python\tfc_face_01.jpg")

plt.imshow(face_im)
plt.axis('off')   # Don't display image axes
plt.title("Face Example")
plt.show()

print("Converting the image to grey-scale")
grey_face = color.rgb2gray(face_im)
print("Image shape: ",grey_face.shape)

plt.imshow(grey_face,cmap='gray')
plt.axis('off')   # Don't display image axes
plt.title("Face Example (Greyscale)")
plt.show()