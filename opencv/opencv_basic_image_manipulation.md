# Introduction

Based on content discussed in the OpenCV Bootcamp from opencv.org

# Import libraries

```python
import os
import cv2
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline

from IPython.display import Image, display

cb_image = cv2.imread("data/checkerboard_18x18.png", 0)

plt.imshow(cb_image, cmap="gray")
print(cb_image)
```

```text

[[  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]
 [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]
 [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]
 [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]
 [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]
 [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]]
```

![Checkerboard pattern](/images/opencv/opencv-checkerboard.png?raw=true "Checkerboard pattern")

# Access individual pixels

```python
print(cb_image[0,0])
print(cb_image[0,6])
```

```text
0
255
```

# Modify pixels

```python
cb_image_copy = cb_image.copy()
cb_image_copy[2,2] = 100
cb_image_copy[2,3] = 100
cb_image_copy[3,2] = 100
cb_image_copy[3,3] = 100

plt.imshow(cb_image_copy, cmap="gray")
print(cb_image_copy)
```

```text
[[  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0 100 100   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0 100 100   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]
 [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]
 [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]
 [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]
 [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]
 [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]]
```

![Checkerboard pattern modified](/images/opencv/opencv-checkerboard-modified.png?raw=true "Checkerboard Pattern modified")

# Cropping images

```python
image_flowers_bgr = cv2.imread("data/flowers.png", cv2.IMREAD_COLOR)
image_flowers_rgb = image_flowers_bgr[:, :, ::-1]

plt.imshow(image_flowers_rgb)
```

![Flower](/images/opencv/opencv-flower.png?raw=true "Flower")

```python
cropped_region = image_flowers_rgb[200:300, 100:200]
plt.imshow(cropped_region)
```
![Flower crop](/images/opencv/opencv-flower-crop.png?raw=true "Flower crop")

