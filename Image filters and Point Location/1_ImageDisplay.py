# -*- coding: utf-8 -*-
"""
Basic image display
"""

import numpy as np
from scipy import misc,ndimage
import matplotlib.pyplot as plt

# Simple image display
face_im = misc.face()

print("Image shape: ",face_im.shape)
plt.imshow(face_im)
plt.title("Example of plt.imshow()")
plt.show()

# Display without the axes
face_im = misc.face()
plt.imshow(face_im)
plt.axis('off')   # Don't display image axes
plt.title("Remove axes")
plt.show()

# Simple image display, forcing load into a float image
face_im = misc.face(gray=True).astype(np.float32)
print("Image shape: ",face_im.shape)

plt.imshow(face_im, cmap=plt.cm.gray)
plt.title("Example of displaying a greyscale image")
plt.axis('off')   # Don't display image axes
plt.show()




