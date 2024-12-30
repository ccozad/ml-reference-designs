# Introduction

Based on lecture material from the OpenCV Bootcamp offered by opencv.org.

# Import libraries

```python
import os
import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

matplotlib.rcParams['figure.figsize'] = (9.0, 9.0)

%matplotlib inline

image = cv2.imread("data/boston.jpg", cv2.IMREAD_COLOR)
plt.imshow(image[:, :, ::-1])
```

![Historical picture of Boston](/images/opencv/opencv-source-image.png?raw=true "Historical picture of Boston")

# Draw lines

```python
image_line = image.copy()

cv2.line(image_line, (200, 100), (400, 100), (0, 255, 255), thickness=2, lineType=cv2.LINE_AA)
cv2.line(image_line, (500, 500), (300, 200), (0, 0, 255), thickness=2, lineType=cv2.LINE_AA)

plt.imshow(image_line[:, :, ::-1])
```
![Lines drawn using OpenCV code](/images/opencv/opencv-source-image.png?raw=true "Lines drawn using OpenCV code")




