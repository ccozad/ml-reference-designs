import os
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
import dotenv
dotenv.load_dotenv()

print("Loading Checkpoint...")
checkpoint = os.getenv("CHECKPOINT")

print("Loading Model Type...")
model_type = os.getenv("MODEL_TYPE")

print("Initializing SAM registry...")
sam = sam_model_registry[model_type](checkpoint=checkpoint)
sam.to("cuda")
mask_generator = SamAutomaticMaskGenerator(sam)
masks = mask_generator.generate("./chickens.jpg")