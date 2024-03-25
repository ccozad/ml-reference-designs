# Introduction

This repo contains a set of reference designs for various ML topics.

# Setup

## Jupyter requirement

The examples in this repo are meant to be run interactively using Jupyter-Lab or Jupiter-Notebooks. See https://jupyter.org/install

## Virtual environment

To avoid conflicts with your local environment, create a virtual environment and run the notebook within this environment.

### Windows
```
python -m venv .venv
.venv\Scripts\activate
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
python -m ipykernel install --user --name=virtualenv
```

### Selecting the new kernel

Then select the virtualenv kernel after launching Jupyter Lab with the command `jupyter lab`

### Additional resources
For additional background see https://www.linkedin.com/pulse/how-use-virtual-environment-inside-jupyter-lab-sina-khoshgoftar

# Contents

## Getting Started

Various simple examples for getting started with different frameworks

- PyTorch
  - [Hello World](/getting-started/pytorch_hello_world.ipynb)
  - [GPU](/getting-started/pytorch_gpu.ipynb)
- TensorFlow
  - [Hello World](/getting-started/tensorflow_hello_world.ipynb)
  - [GPU (Linux only)](/getting-started/tensorflow_gpu.ipynb)

## Feature Engineering

Various recipes for common feature engineering tasks.

- [Pandas essentials](/feature-engineering/pandas_essentials.ipynb)
- [Handle missing data](/feature-engineering/handle_missing_data.ipynb)
- [Choose fourier features](/feature-engineering/choosing_fourier_features.ipynb)
- [Kaggle predict home price feature prep](/linear-regression/kaggle-predict-house-price-data-prep.ipynb)

## Regression

 - [Kaggle predict home prices with PyTorch](/linear-regression/kaggle-predict-house-prices.ipynb)

## Computer Vision

Various examples that deal with processing image data.

- [Image classification with PyTorch and Fashion MNIST](/computer-vision/pytorch-fashionMNIST.ipynb)

## Deployment

Various tasks that deal with using trained models

- [Kaggle predict home prices, batch evaluate blind test data](/linear-regression/kaggle-predict-house-price-evaluation.ipynb)
