import os
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
import numpy as np
import cv2

import dotenv
dotenv.load_dotenv()

# Set the seed for reproducibility
np.random.seed(0)

print("Loading Checkpoint...")
checkpoint = os.getenv("CHECKPOINT")

print("Loading Model Type...")
model_type = os.getenv("MODEL_TYPE")

def draw_segments(anns):
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)

    # Create an empty image
    # Match the data type with our source image so we can overlay the masks
    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4), dtype=np.uint8)
    # Set the alpha channel to 0
    img[:,:,3] = 0
    for ann in sorted_anns:
        m = ann['segmentation']
        # Generate a random color for the mask
        color_mask = np.concatenate([np.random.random(3), [1]]) * 255
        img[m] = color_mask
    
    return img

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
image_alpha = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)
image_alpha[:, :, 3] = 255
segments = draw_segments(masks)

print("Combining images with segmentation masks...")
combined_image = cv2.addWeighted(image_alpha, 1, segments, 0.95, 0)

print("Saving output image...")
cv2.imwrite("output.jpg", cv2.cvtColor(combined_image, cv2.COLOR_RGB2BGR))
