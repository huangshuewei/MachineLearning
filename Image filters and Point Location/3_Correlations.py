# -*- coding: utf-8 -*-
"""
Examples of filtering images.
"""

import numpy as np
from scipy import misc,ndimage
import matplotlib.pyplot as plt
from skimage import io,color
from skimage.transform import downscale_local_mean

# Load image as grey-scale and convert to type float
face_im = color.rgb2gray(io.imread('MR_bean.jpg')).astype(np.float32)

plt.imshow(face_im, cmap=plt.cm.gray)
plt.axis('off')   # Don't display image axes
plt.title("Original Face Image")
plt.show()

# Smoothing with a Gaussian filter
smoothed_face_sd3 = ndimage.gaussian_filter(face_im, sigma=3)
plt.imshow(smoothed_face_sd3, cmap=plt.cm.gray)
plt.axis('off')   # Don't display image axes
plt.title("Smoothed with Gaussian (SD=5)")
plt.show()

# Downscale image
face_im2=downscale_local_mean(face_im,(2,2))


# Basic gradient filters
xgrad_filter=np.array([[-1,0,1]], dtype=np.float32)
ygrad_filter=np.array([[-1],[0],[1]], dtype=np.float32)

# Apply filters
face_gx=ndimage.convolve(face_im2,xgrad_filter)
face_gy=ndimage.convolve(face_im2,ygrad_filter)

# Gradient magnitude
face_g=np.sqrt(face_gx**2 + face_gy**2)

fig2 = plt.figure(figsize = (12,12)) # Create a large figure
ax = fig2.add_subplot(2,2,1)
ax.imshow(face_im2, cmap=plt.cm.gray)
ax.set_title("Original Patch")
ax.axis('off')
ax = fig2.add_subplot(2,2,2)
ax.imshow(face_gx, cmap=plt.cm.gray)
ax.set_title("x-gradient")
ax.axis('off')
ax = fig2.add_subplot(2,2,3)
ax.imshow(face_gy, cmap=plt.cm.gray)
ax.set_title("y-gradient")
ax.axis('off')
ax = fig2.add_subplot(2,2,4)
ax.imshow(face_g, cmap=plt.cm.gray)
ax.set_title("Gradient magitude")
ax.axis('off')

plt.show()


