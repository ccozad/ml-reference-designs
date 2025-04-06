# Introduction

This repo contains a set of reference designs for various ML topics. A few examples of the types of things you can learn here:

# Contents

## Broswer Use [FEATURED]

Browser Use is an open source library that allows language models to interact with browser windows and page contents

- [Overview and Setup](/browser-use/)
- [Gather Car Prices](/browser-use/find_car_prices.py)

[![Browser Use Demo - Gather Car Prices](https://img.youtube.com/vi/rDLlWlCFW6A/0.jpg)](https://www.youtube.com/watch?v=rDLlWlCFW6A)

## Agents [FEATURED]

An Agent is a system that leverages an AI model to interact with its environment in order to achieve a user-defined objective. It combines reasoning, planning, and the execution of actions (often via external tools) to fulfill tasks.
 
 - [Overview](/agents/)
 - [Dummy Agent](/agents/dummy-agent/) A bare bones agent with mocked tool calls 
 - [Smol Agent](/agents/smol-agent/) A template for using the SmolAgent framework with a Gradio web interface
 - [Code Agents](/agents/code-agents/) Use the SmolAgent framework to create agents that generate code to call tools and perform calculations.
   - [Duration Agent](/agents/code-agents/duration_agent.py) Generate code that uses authorized imports to add up the times listed in the prompt.
   - [Menu Agent](/agents/code-agents/menu_agent.py) Call a custom tool to generate a menu prompt and populate using the model's built in knowledge
   - [Playlist Agent](/agents/code-agents/playlist_agent.py) Search the internet and generate a music playlist for a wedding
 - [Workout Agents](/agents/workout-agents/) Use the SmolAgent framework to perform fitness related planning tasks
   - [Strength Plan Agent](/agents/workout-agents/strength_plan_agent.py) An agent that considers how many reps you can do at a given weight and generates a strength training program
- [Retrieval Agents](/agents/retrieval-agents/) Retrieve data from specialized systems using the SmolAgent framework.
   - [Basic Retrieval Agent](/agents/retrieval-agents/basic_retrieval_agent.py) Search the internet using Duck Duck Go and form a total body fitness plan
   - [NIST CSF Retrieval Agent](/agents/retrieval-agents/nist_csf_retrieval_agent.py) Use semantic search (search by meaning) against specialized NIST Cyber Security Framework practices
 - [Multi-agents](/agents/multi-agents/) Multiple agents working together
   - [Park Planner Multi-Agent](/agents/multi-agents/park_planner_multi_agent.py) Search the internet for national parks and calculate travel time by cargo plane. One agent can search the internet and the other agent does planning and distance calculations
 - [Travel Agents](/lang-graph/travel-agent/) Use LangGraph to work with natural language to work with flight reservations and look up company travel policies
   - [Zero-shot Agent](/lang-graph/travel-agent/zero_shot_agent.py) Perform all of the steps at once without confirmation by the user
   - [Confirmation Agent](/lang-graph/travel-agent/confirmation_agent.py) Confirm with the user before every tool call
   - [Smart Confirm Agent](/lang-graph/travel-agent/smart_confirm_agent.py) Only confirm with the user before writing to the database

Leverage agents that use a large language model as the brain to direct tools that interact with the real world.
![AI Agent](/images/ai-agents.png?raw=true "AI Agent")

## Getting Started

Various simple examples for getting started with different frameworks

- [Terminology](/general/terminology.md)
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
- [Choose Fourier features](/scikit-learn/time-series/choosing_fourier_features.ipynb)
- [Kaggle predict home price feature prep](/pytorch/home-prices/kaggle-predict-house-price-data-prep.ipynb)

## Image Processing

Recipes for working with images

- [OpenCV essentials](/opencv/opencv_essentials.ipynb)
- [OpenCV basic image manipulation](/opencv/opencv_basic_image_manipulation.md)
- [OpenCV annotate images](/opencv/opencv_annotate_images.md)
- [OpenCV image enhancement](/opencv/opencv_image_enhancement.ipynb)

Increase the effectiveness of OCR by preprocessing images
![Adaptive threshold](/images/image-processing/adaptive-threshold.png?raw=true "Adaptive threshold")

## Regression

Various examples that deal with predicting a value based on inputs

- [Synthetic regression with PyTorch](/pytorch/synthetic-regression/pytorch_synthetic_regression.ipynb)
- [Kaggle predict home prices with PyTorch](/pytorch/home-prices/kaggle-predict-house-prices.ipynb)

## Classification

Various examples that deal with placing inputs into one or more categories

- [Classify breast cancer diagnosis with PyTorch](/general/imbalanced_classification.ipynb)
- [Image classification with PyTorch and Fashion MNIST](/pytorch/fashion-mnist/pytorch-fashionMNIST.ipynb)
- [Sentiment analysis in JavaScript using transformers](/huggingface/sentiment-analysis-js/)

## Clustering

Various examples that deal with grouping data points by a similarity metric.
- [Cluster seed types using K-Means and scikit-learn](/scikit-learn/clustering/kmeans_clustering.md)
- [Cluster penguin species using DBSCAN and scikit-learn](/scikit-learn/clustering/dbscan_clustering.md)

Group items that are similar using only their attributes
![K-means clustering for seeds](/images/kmeans/seeds-kmeans.png?raw=true "K-means clustering for seeds")

## Time Series

Various examples that deal with time based data

- [Forecast seasonal airline traffic using scikit-learn](/scikit-learn/time-series/choosing_fourier_features.ipynb)

Predict future values in data that varies over time
![Time Series Prediction](/images/time-series-prediction.png?raw=true "Time Series Prediction")

## Computer Vision

Various examples that deal with processing image data.

- [Image classification with PyTorch and Fashion MNIST](/pytorch/fashion-mnist/pytorch-fashionMNIST.ipynb)
- [Image segmentation using the Meta Segment Anything Model and OpenCV](/segment-anything-model/)

Intelligently select complex objects in images
![Segmented Image](/images/sam-example.jpg?raw=true "Segmented Image")

## Large Language Models

Examples that interact with large language models with billions of parameters that are often training across many commercial grade GPUs for many millions of hours.

### Claude 3.5
 - [Claude 3.5 Hello World](/llm/claude-3-5/hello-world/)
 - [Claude 3.5 Tool Calling](/llm/claude-3-5/tool-calling/)

### LangChain
- [LangChain terminology](/lang-chain/terminology.md)
- [RAG based Q&A](/lang-chain/RAG/)
  - [Index web page data using BeautifulSoup, OpenAI Embeddings and Chroma](/lang-chain/RAG/index_pipeline.py)
  - [Neo4j Graph RAG](/lang-chain/Neo4j/)
  - [Retrieval Augmented Generation (RAG) Q&A pipeline using OpenAI Embeddings, OpenAI Chat and Chroma](/lang-chain/RAG/rag_pipeline.py)
  - [RAG Q&A pipeline using Hugging Face Embeddings, Amazon Bedrock with Meta Llama 3 foundation model and Chroma](/lang-chain/AWS-Bedrock/)

Direct a large language model to answer based only on context from documents
![RAG Pipeline](/images/rag-pipeline.png?raw=true "RAG Pipeline")

### LangGraph
- [LangGraph terminology](/lang-graph/terminology.md)
- [LangGraph simple graph, sentiment response](/lang-graph/sentiment/)
- [LangGraph travel agent](/lang-graph/travel-agent/)

Form graphs to model decisions and loops with AI
![Positive Sentiment Trace](/images/positive-sentiment-trace.png?raw=true "Positive Sentiment Trace")

### Llama 3

- [Local Llama 3 chat demo](/llm/llama-3/hello-llama-3.ipynb)
- [Run Llama 3 on an AWS EC2 instance](/llm/llama-3/hello-world/README.md)

### Llama Index

- [Call ChatGPT with a prompt template](/llama-index/llm/)

## Small Language Models

### Phi-3

- [Phi-3 demo](/slm/phi-3/hello-world/)
- [SmoLM2 Story Writer](/slm/smollm2/story-writer/)

## Deployment

Various tasks that deal with deploying AI systems

- [Kaggle predict home prices, batch evaluate blind test data](/pytorch/home-prices/kaggle-predict-house-price-evaluation.ipynb)
- [Run Llama 3 on an AWS EC2 instance](/llm/llama-3/hello-world/)
- [Run LLM pipeline Python code in a container using Docker](/lang-chain/docker-serve/)
- [Serve index and RAG pipelines over HTTP using Flask](/lang-chain/RAG-serve/)
- [Use the Model Context Protocol (MCP) with a custom LLM client and data access server](/mcp/client-py/)

# Setup

## Jupyter requirement

Some of the examples in this repo are meant to be run interactively using Jupyter-Lab or Jupiter-Notebooks. See https://jupyter.org/install

Examples that only have script files will have a README file with instructions.

## Python Virtual environment

To avoid conflicts with your local environment, create a virtual environment and run the notebook within this environment.

### Selecting the new kernel

Then select the virtualenv kernel after launching Jupyter Lab with the command `jupyter lab`

### Additional resources
For additional background see https://www.linkedin.com/pulse/how-use-virtual-environment-inside-jupyter-lab-sina-khoshgoftar

### Windows
```
python -m venv .venv
.venv\Scripts\activate
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
python -m ipykernel install --user --name=virtualenv
```

Most advances in machine learning are happening on Linux targeting Nvidia GPUs with CUDA support. Some advanced models such as Llama 3 may not work well (or at all) on Windows machines.

## JavaScript environment

Some examples are targeted at NodeJS. There are no specific versions of Node needed but you can always use `nvm` to keep your environments tidy. See https://github.com/nvm-sh/nvm for more details.

## Working with LLMs

Workbook examples that include LLMs models are more complex than other examples and require additional setup work.

**Llama 3**
 - Download the model weights (requires an access request that is granted by Meta staff, may take 24 hours or more to be approved) https://huggingface.co/meta-llama/Meta-Llama-3-8B
 - Model weights are GBs of data, store them in a drive with sufficient space
 - Clone the model code https://github.com/meta-llama/llama3
 - Change to the directory with the model code and pip install the model and dependencies `pip install -e .`


# Further Reading

- [Agents in Software Engineering: Survey, Landscape, and Vision](https://github.com/DeepSoftwareAnalytics/Awesome-Agent4SE)
- [Attention Is All You Need](https://arxiv.org/pdf/1706.03762)
- [Let's build ChatGPT: from scratch, in code, spelled out, Andrej Karpathy](https://www.youtube.com/watch?v=kCc8FmEb1nY)
- [Model Context Protocol](https://github.com/modelcontextprotocol)
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://react-lm.github.io/)
- [SmolLM Github](https://github.com/huggingface/smollm)

# Industry domain problems

Examples in this repo cover the following industry domain problems:

 - Accounting
   - Receipt processing
 - Botany
   - Group observations into n groups based on equal variance
 - Customer Service
   - Context aware chat bots
 - Event Planning
   - Generate music playlists
   - Generate menus for specific occasions
   - Calculate the total time needed for setup
 - Fitness
   - Generate a strength training program
 - Games
   - AI controlled NPCs 
 - Hospitality
   - Sentiment analysis
 - Medical
   - Breast cancer diagnosis
 - Real Estate
   - Price prediction
 - Retail
   - Product image classification
 - Technology
   - Deploy machine learning models to production
   - Compose workflows involving large language models (LLMs)
   - Store and search for embedding data in vector stores
   - Intelligently select complex objects in images
   - Expand capabilities of large language models with custom tool calling
   - Create AI agents that can interact with the real world
 - Transportation
   - Seasonal airline traffic prediction
   - Search the internet for locations, calculate travel times to all destinations
   - Manage flights
 - Zoology
   - Group observations based on data density