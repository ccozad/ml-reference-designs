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
![Lines drawn using OpenCV code](/images/opencv/opencv-lines.png?raw=true "Lines drawn using OpenCV code")

# Draw circles

```python
image_circle = image.copy()

cv2.circle(image_circle, (200, 200), 50, (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

plt.imshow(image_circle[:, :, ::-1])
```

![Circles drawn using OpenCV code](/images/opencv/opencv-circles.png?raw=true "Circles drawn using OpenCV code")

# Draw rectangles

```python
image_rectangle = image.copy()

cv2.rectangle(image_rectangle, (300, 300), (400, 400), (176, 200, 12), thickness=2, lineType=cv2.LINE_8)

plt.imshow(image_rectangle[:, :, ::-1])
```

![Rectangles drawn using OpenCV code](/images/opencv/opencv-rectangles.png?raw=true "Rectangles drawn using OpenCV code")

# Add text

```python
image_text = image.copy()
text = "Boston, 1906"
font_scale = 2.0
font_face = cv2.FONT_HERSHEY_PLAIN
font_color = (0, 255, 255)
font_thickness = 2

cv2.putText(image_text, text, (200, 485), font_face, font_scale, font_color, font_thickness, cv2.LINE_AA)

plt.imshow(image_text[:, :, ::-1])
```

![Text drawn using OpenCV code](/images/opencv/opencv-text.png?raw=true "Text drawn using OpenCV code")