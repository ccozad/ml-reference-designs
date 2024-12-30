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

# Resizing images

```python
resized_cropped_region_2x = cv2.resize(cropped_region, None, fx=2, fy=2)
plt.imshow(resized_cropped_region_2x)
```

![Flower resize](/images/opencv/opencv-flower-crop-resize.png?raw=true "Flower resize")

```python
desired_width = 100
desired_height = 200
dim = (desired_width, desired_height)

resized_cropped_region = cv2.resize(cropped_region, dsize=dim, interpolation=cv2.INTER_AREA)
plt.imshow(resized_cropped_region)
```
![Flower resize stretch](/images/opencv/opencv-flower-crop-resize2.png?raw=true "Flower resize stretch")

```python
desired_width = 100
aspect_ratio = desired_width / cropped_region.shape[1]
desired_height = int(cropped_region.shape[0] * aspect_ratio)
dim = (desired_width, desired_height)

resized_cropped_region = cv2.resize(cropped_region, dsize=dim, interpolation=cv2.INTER_AREA)
plt.imshow(resized_cropped_region)
```

![Flower resize](/images/opencv/opencv-flower-crop-resize.png?raw=true "Flower resize")

```python
resized_cropped_region_2x = resized_cropped_region_2x[:, :, ::-1]
cv2.imwrite("resized_cropped_region_2x.png", resized_cropped_region_2x)
Image(filename="resized_cropped_region_2x.png")
```

![Flower resize medium](/images/opencv/opencv-flower-resize-medium.png?raw=true "Flower resize medium")


```python
cropped_region = cropped_region[:, :, ::-1]
cv2.imwrite("cropped_region.png", cropped_region)
Image(filename="cropped_region.png")
```

![Flower resize small](/images/opencv/opencv-flower-resize-small.png?raw=true "Flower resize small")


# Flip images

```python
image_flowers_rgb_flipped_horiz = cv2.flip(image_flowers_rgb, 1)
image_flowers_rgb_flipped_vert = cv2.flip(image_flowers_rgb, 0)
image_flowers_rgb_flipped_both = cv2.flip(image_flowers_rgb, -1)

plt.figure(figsize=(18,5))

plt.subplot(141)
plt.imshow(image_flowers_rgb_flipped_horiz)
plt.title("Horizontal Flip")

plt.subplot(142)
plt.imshow(image_flowers_rgb_flipped_vert)
plt.title("Vertical Flip")

plt.subplot(143)
plt.imshow(image_flowers_rgb_flipped_both)
plt.title("Both Flipped")

plt.subplot(144)
plt.imshow(image_flowers_rgb)
plt.title("Original")
```
![Flower flip](/images/opencv/opencv-flower-flip.png?raw=true "Flower flip")
