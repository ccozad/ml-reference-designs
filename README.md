# Introduction

This repo contains a set of reference designs for various ML topics. References for futher reading are provided with each example.

# Jupyter requirement

The examples in this repo are meant to be run interactively using Jupyter-Lab or Jupiter-Notebooks. See https://jupyter.org/install

# Virtual environment

To avoid conflicts with your local environment, create a virtual environment and run the notebook within this environment.

## Windows
```
python -m venv .venv
.venv\Scripts\activate
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
python -m ipykernel install --user --name=virtualenv
```

## Selecting the new kernel

Then select the virtualenv kernel after launching Jupyter Lab with the command `jupyter lab`

## Additional resources
For additional background see https://www.linkedin.com/pulse/how-use-virtual-environment-inside-jupyter-lab-sina-khoshgoftar 