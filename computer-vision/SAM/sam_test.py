import os
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
import numpy as np
import cv2
import matplotlib.pyplot as plt

import dotenv
dotenv.load_dotenv()

print("Loading Checkpoint...")
checkpoint = os.getenv("CHECKPOINT")

print("Loading Model Type...")
model_type = os.getenv("MODEL_TYPE")

def show_anns(anns):
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)

    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
    img[:,:,3] = 0
    for ann in sorted_anns:
        m = ann['segmentation']
        color_mask = np.concatenate([np.random.random(3), [0.35]])
        img[m] = color_mask
    ax.imshow(img)

def draw_segments(image, anns):
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)

    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
    img[:,:,3] = 0
    for ann in sorted_anns:
        m = ann['segmentation']
        color_mask = np.concatenate([np.random.random(3), [0.35]])
        img[m] = color_mask
    ax.imshow(img)

print("Loading Image...")
image = cv2.imread("./chickens.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print("Initializing SAM registry...")
sam = sam_model_registry[model_type](checkpoint=checkpoint)
sam.to("cuda")
mask_generator = SamAutomaticMaskGenerator(sam)

print("Generating masks...")
masks = mask_generator.generate(image)

print("Drawing masks...")
plt.imshow(image)
show_anns(masks)
plt.axis('off')
plt.show() 
#for i, mask in enumerate(masks):
#    segments = mask['segmentation']
#    j = 0
#    for seg in segments:
#        if j < 3:
#            print(seg)
            #cv2.drawContours(image, seg, -1, (255, 0, 0), 2)
#            j += 1
        #cv2.drawContours(image, seg, -1, (0, 255, 0), 2)
    #cv2.rectangle(image, (mask['bbox'][0], mask['bbox'][1]), (mask['bbox'][2], mask['bbox'][3]), (255, 0, 0), 2)
        #print(mask)
        #segments = [np.array(seg, np.int32).reshape((1, -1, 2)) for seg in mask['segmentation']]
        #for seg in segments:
            #cv2.drawContours(image, seg, -1, (0, 255, 0), 2)

cv2.imwrite("output.jpg", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
