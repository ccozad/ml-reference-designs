# Introduction

Segmentation is the computer vision task of identifying the pixel level boundary or mask of an object in an image.

Meta AI Research has developed a foundation model called the Segment Anything Model or SAM that make high quality, zero shot segmentaton masks on unfamiliar objects and images. The model was trained on over a billion segmentation masks across ~11 million images.

An example of a segmented image:

![Segmented Image](/images/sam-example.png?raw=true "Segmented Image")

# Dependencies

All of the dependencies listed below need to be in place before running the code.

 - Access to GPU and CUDA drivers
 - Python virtual environment
 - PyTorch and TorchVision with CUDA support
 - Install segment anything
 - Download SAM checkpoint
 - Environment Variables

## Access to GPU and CUDA drivers

Processing large images for pixel level features is a compute intense task that is best done a machine with a GPU and suitable CUDA drivers. You can install the CUDA driver and supporting tools by downloading and installing the CUDA Toolkit from Nvidia: https://developer.nvidia.com/cuda-toolkit 

When the correct drivers are installed, PyTorch will automatically use the accelerated GPU compute path.

Confirm your installation with by checking the Nvidia CUDA Compiler Version

```
nvcc --version
```

You will get output similar to the following:

```
nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Tue_Aug_15_22:09:35_Pacific_Daylight_Time_2023
Cuda compilation tools, release 12.2, V12.2.14
```

## Python Virtual Environment

 - Move to the RAG folder
   - `cd <computer-vision/SAM>`
 - Create a virtual environment
   - On Mac: `python3 -m venv .venv`
   - On Windows: `python -m venv .venv`
 - Activate the virtual environment
   - On Mac: `source .venv/bin/activate`
   - On Windows: `.venv\Scripts\activate`
 - Install dependencies
   - On Mac: `pip3 install -r requirements.txt`
   - On Windows: `pip install -r requirements.txt`
 - Call a specific script
   - On Mac: `python3 <script_name>.py`
   - On Windows: `python <script_name>.py`
 - Deactivate virtual environment
   - `deactivate`

## PyTorch and Torchvision with CUDA support

PyTorch and TorchVision with CUDA support can be installed by using the command generator on the PyTorch website. After you finish your installation you can check that everything works by running the `check_env.py` script.

Example output for the `check_env.py` script

```
CUDA is available: True
Number of devices: 1
Current device: 0
Active device: <torch.cuda.device object at 0x000002675729BF40>
Device name: NVIDIA GeForce RTX 3060
```

## Install Segment Anything

Refer to the SegmentAnything GitHub https://github.com/facebookresearch/segment-anything for details or simple run:

```shell
pip install git+https://github.com/facebookresearch/segment-anything.git
```

## Download SAM checkpoint

The largest model checkpoints are more than 2 GB in size. Download the checkpoints from https://github.com/facebookresearch/segment-anything/blob/main/README.md#model-checkpoints


## Environment Variables

Create a file named `.env` with the contents shown below. Replace the values based on how your machine is configured.

```
CHECKPOINT=<path to your checkpoint>
MODEL_TYPE=<vit_h | vit_l | vit_b>
```