# -*- coding: utf-8 -*-
"""
Searching for a target with a kernel.
Create a kernel by cropping an image.
Use correlation to search image for good matches.
"""

import numpy as np
from scipy import misc,ndimage
import matplotlib.pyplot as plt
from skimage import io,color
from skimage.transform import downscale_local_mean

# Load image as grey-scale and convert to type float
face_im_full = color.rgb2gray(io.imread('swh_face1.jpg')).astype(np.float32)

# Downscale image for speed
face_im=downscale_local_mean(face_im_full,(1,1))


# Target centre 
#p=[125, 125] # Right eye
p=[79, 180] # Nose tip
#p=[162, 162] # Right mouth corner

plt.imshow(face_im, cmap=plt.cm.gray)
plt.plot(p[0],p[1],"o",color="yellow")
plt.axis('off')   # Don't display image axes
plt.title("Original Face Image")
plt.show()

# Half-width of region to crop
# w=17
w=30

# Crop patch.
# Note use (y,x) because image represented as matrix
patch=face_im[p[1]-w:p[1]+w,p[0]-w:p[0]+w]

# Remove mean value
patch=patch-patch.mean()

plt.imshow(patch,cmap=plt.cm.gray)
plt.axis('off')   # Don't display image axes
plt.title("Patch")
plt.show()

# Load image as grey-scale and convert to type float
face_im2_full = color.rgb2gray(io.imread('swh_face2.jpg')).astype(np.float32)

# Downscale image for speed
face_im2=downscale_local_mean(face_im2_full,(1,1))

result=ndimage.correlate(face_im2,patch)

# Find the position of the peak (maximum)
# np.argmax() returns index as single integer
# np.unravel_index converts that into the (i,j) position
max_p=np.unravel_index(np.argmax(result, axis=None), result.shape)
print("Max response at ",max_p)

fig2 = plt.figure(figsize = (12,12)) # Create a large figure
ax = fig2.add_subplot(1,2,1)
ax.imshow(face_im2, cmap=plt.cm.gray)
ax.plot(max_p[1],max_p[0],"x",color="red")
ax.set_title("Original Image")
ax.axis('off')
ax = fig2.add_subplot(1,2,2)
ax.imshow(result, cmap=plt.cm.gray)
ax.plot(max_p[1],max_p[0],"x",color="red")
ax.set_title("Response")
ax.axis('off')
plt.show()

