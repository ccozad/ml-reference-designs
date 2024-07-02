# Introduction

This repo contains a set of reference designs for various ML topics. A few examples of the types of things you can learn here:

Direct a large language model to answer based only on context from documents
![RAG Pipeline](/images/rag-pipeline.png?raw=true "RAG Pipeline")

Intelligently select complex objects in images
![Segmented Image](/images/sam-example.jpg?raw=true "Segmented Image")

Predict future values in data that varies over time
![Time Series Prediction](/images/time-series-prediction.png?raw=true "Time Series Prediction")

# Industry domain problems

Examples in this repo cover the following industry domain problems:

 - Accounting
   - Receipt processing
 - Botany
   - Group observations into n groups based on equal variance
 - Customer Service
   - Context aware chat bots
 - Medical
   - Breast cancer diagnosis
 - Real Estate
   - Price prediction
 - Retail
   - Product image classification
 - Technology
   - Deploy machine learning models to production
   - Compose workflows involving large language models (LLMs)
   - Store and search for embedding data in vectorstores
   - Intelligently select complex objects in images
   - Expand capabilities of large language models with custom tool calling
 - Transportation
   - Seasonal airline traffic prediction
 - Zoology
   - Group observations based on data density

# Setup

## Jupyter requirement

Some of the examples in this repo are meant to be run interactively using Jupyter-Lab or Jupiter-Notebooks. See https://jupyter.org/install

Examples that only have script files will have a README file with instructions.

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

Most advances in machine learning are happing on Linux targeting Nvidia GPUs with CUDA support. Some advanced models such as Llama 3 may not work well (or at all) on Windows machines.

### Working with LLMs

Workbook examples that include LLMs models are more complex than other examples and require additional setup work.

**Llama 3**
 - Download the model weights (requires an access request that is granted by Meta staff, may take 24 hours or more to be approved) https://huggingface.co/meta-llama/Meta-Llama-3-8B
 - Model weights are GBs of data, store them in a drive with sufficient space
 - Clone the model code https://github.com/meta-llama/llama3
 - Change to the directory with the model code and pip install the model and dependencies `pip install -e .`

### Selecting the new kernel

Then select the virtualenv kernel after launching Jupyter Lab with the command `jupyter lab`

### Additional resources
For additional background see https://www.linkedin.com/pulse/how-use-virtual-environment-inside-jupyter-lab-sina-khoshgoftar

# Contents

## Getting Started

Various simple examples for getting started with different frameworks

- [Terminology](/general/terminology.ipynb)
- PyTorch
  - [Hello World](/pytorch/getting-started/pytorch_hello_world.ipynb)
  - [GPU](/pytorch/getting-started/pytorch_gpu.ipynb)
  - [Tensor operations](/pytorch/getting-started/pytorch_tensor_operations.ipynb)
  - [Auto differentiation](/pytorch/getting-started/pytorch_auto_differentiation.ipynb)
  - [Getting help](/pytorch/getting-started/pytorch_getting_help.ipynb)
- TensorFlow
  - [Hello World](/tensor-flow/getting-started/tensorflow_hello_world.ipynb)
  - [GPU (Linux only)](/tensor-flow/getting-started/tensorflow_gpu.ipynb)

## Feature Engineering

Various recipes for common feature engineering tasks.

- [Pandas essentials](/general/pandas_essentials.ipynb)
- [Handle missing data](/general/handle_missing_data.ipynb)
- [Convert class labels to numbers](/general/convert_class_to_numeric.ipynb)
- [Imbalanced classification](/general/imbalanced_classification.ipynb)
- [Choose Fourier features](/general/choosing_fourier_features.ipynb)
- [Kaggle predict home price feature prep](/pytorch/home-prices/kaggle-predict-house-price-data-prep.ipynb)

## Image Processing

Recipes for working with images

- [OpenCV essentials](/opencv/opencv_essentials.ipynb)
- [OpenCV basic image manipulation](/opencv/opencv_basic_image_manipulation.ipynb)
- [OpenCV annotate images](/opencv/opencv_annotate_images.ipynb)
- [OpenCV image enhancement](/opencv/opencv_image_enhancement.ipynb)

## Regression

Various examples that deal with predicting a value based on inputs

- [Synthetic regression with PyTorch](/pytorch/synthetic-regression/pytorch_synthetic_regression.ipynb)
- [Kaggle predict home prices with PyTorch](/pytorch/home-prices/kaggle-predict-house-prices.ipynb)

## Classification

Various examples that deal with placing inputs into one or more categories

- [Classify breast cancer diagnosis with PyTorch](/general/imbalanced_classification.ipynb)
- [Image classification with PyTorch and Fashion MNIST](/pytorch/fashion-mnist/pytorch-fashionMNIST.ipynb)

## Clustering

Various examples that deal with grouping data points by a similarity metric.
- [Cluster seed types using K-Means and scikit-learn](/scikit-learn/clustering/kmeans_clustering.ipynb)
- [Cluster penguin species using DBSCAN and scikit-learn](/scikit-learn/clustering/dbscan_clustering.ipynb)

## Time Series

Various examples that deal with time based data

- [Forecast seasonal airline traffic using scikit-learn](/general/choosing_fourier_features.ipynb)

## Computer Vision

Various examples that deal with processing image data.

- [Image classification with PyTorch and Fashion MNIST](/pytorch/fashion-mnist/pytorch-fashionMNIST.ipynb)
- [Image segmentation using the Meta Segment Anything Model and OpenCV](/SAM/README.md)

## Large Language Models

Examples that interact with large language models with billions of parameters that are often training across many commercial grade GPUs for many millions of hours.

### Claude 3.5
 - [Claude 3.5 Hello World](/llm/claude-3-5/hello-world/)
 - [Claude 3.5 Tool Calling](/llm/claude-3-5/tool-calling/README.md)

### LangChain
- [LangChain Terminology](/lang-chain/terminology.md)
- [RAG based Q&A](/lang-chain/RAG/README.md)
  - [Index web page data using BeautifulSoup, OpenAI Embeddings and Chroma](/lang-chain/RAG/index_pipeline.py)
  - [Retrieval Augmented Generation (RAG) Q&A pipeline using OpenAI Embeddings, OpenAI Chat and Chroma](/lang-chain/RAG/rag_pipeline.py)
  - [RAG Q&A pipeline using Hugging Face Embeddings, Amazon Bedrock with Meta Llama 3 foundation model and Chroma](/lang-chain/AWS-Bedrock/README.md)

### Llama 3

- [Local Llama 3 chat demo](/llm/llama-3/hello-llama-3.ipynb)
- [Run Llama 3 on an AWS EC2 instance](/llm/llama-3/hello-world/README.md)

### Phi-3

- [Phi-3 demo](/llm/phi-3/hello-world/README.md)

## Deployment

Various tasks that deal with using trained models

- [Kaggle predict home prices, batch evaluate blind test data](/pytorch/home-prices/kaggle-predict-house-price-evaluation.ipynb)
- [Run Llama 3 on an AWS EC2 instance](/llm/llama-3/hello-world/README.md)
- [Serve index and RAG pipelines over HTTP using Flask](/lang-chain/RAG-serve/README.md)
- [Run LLM pipeline Python code in a container using Docker](/lang-chain/docker-serve/README.md)