# Notebooks → Standalone Python

The repo's stated direction is to move away from Jupyter notebooks toward standalone Python scripts. The newer agent / LLM / RAG content already follows this convention; the older feature-engineering, PyTorch, OpenCV, and TensorFlow content has not yet been migrated.

## Inventory (20 notebooks)

### `general/` (4)
- `general/convert_class_to_numeric.ipynb`
- `general/handle_missing_data.ipynb`
- `general/imbalanced_classification.ipynb`
- `general/pandas_essentials.ipynb`

### `opencv/` (2)
- `opencv/opencv_essentials.ipynb`
- `opencv/opencv_image_enhancement.ipynb`

Note that `opencv/` already mixes notebooks and `.md` walkthroughs (`opencv_basic_image_manipulation.md`, `opencv_annotate_images.md`) — converting the remaining two would unify the format.

### `pytorch/getting-started/` (5)
- `pytorch/getting-started/pytorch_hello_world.ipynb`
- `pytorch/getting-started/pytorch_gpu.ipynb`
- `pytorch/getting-started/pytorch_tensor_operations.ipynb`
- `pytorch/getting-started/pytorch_auto_differentiation.ipynb`
- `pytorch/getting-started/pytorch_getting_help.ipynb`

### `pytorch/` (other, 3)
- `pytorch/fashion-mnist/pytorch-fashionMNIST.ipynb`
- `pytorch/synthetic-regression/pytorch_synthetic_regression.ipynb`
- `pytorch/home-prices/kaggle-predict-house-price-data-prep.ipynb`
- `pytorch/home-prices/kaggle-predict-house-prices.ipynb`
- `pytorch/home-prices/kaggle-predict-house-price-evaluation.ipynb`

### `scikit-learn/time-series/` (1)
- `scikit-learn/time-series/choosing_fourier_features.ipynb`

### `tensor-flow/getting-started/` (2)
- `tensor-flow/getting-started/tensorflow_hello_world.ipynb`
- `tensor-flow/getting-started/tensorflow_gpu.ipynb`

### `llm/llama-3/` (1)
- `llm/llama-3/hello-llama-3.ipynb` — duplicates the more readable `llm/llama-3/hello-world/` README + `hello.py`. Strong candidate for **delete** rather than convert.

## Conversion approach per notebook

Most of these notebooks intersperse markdown explanation with code cells. There are two reasonable conversion patterns:

1. **Script + README**: Move narrative markdown into a `README.md` next to a single `.py` script. This matches what the LLM / agent examples do today and is the most consistent with current repo direction.
2. **Script with sectioned `print()` output**: Keep narrative as comments and rely on `print()` statements to break up sections. Less rich than a README but quicker to write.

Pattern (1) is recommended — readers tend to land on the GitHub-rendered README, and inline images already work in markdown via the `images/` folder.

## Suggested conversion batches

Group by section so a single PR can update the top-level README links once:

- **Batch A**: `pytorch/getting-started/` (5 notebooks → 5 scripts + 1 README)
- **Batch B**: `pytorch/home-prices/` + `pytorch/synthetic-regression/` + `pytorch/fashion-mnist/`
- **Batch C**: `general/` (4 notebooks)
- **Batch D**: `opencv/` (2 notebooks; merge with existing `.md` walkthroughs)
- **Batch E**: `tensor-flow/` + `scikit-learn/time-series/`
- **Batch F**: Delete or merge `llm/llama-3/hello-llama-3.ipynb`

Each batch becomes one issue.

## Things to watch when converting

- The PyTorch getting-started notebooks likely use `%matplotlib inline` or display tensors as cell output. In a script, results need explicit `print()` and `plt.savefig(...)` (or `plt.show()` if interactive demo is fine). Saving figures into `images/` keeps READMEs renderable on GitHub.
- The home-prices notebooks reference Kaggle CSVs — confirm the download path / instructions are still accurate during conversion.
- The TensorFlow GPU notebook is Linux-only per its title; flag this in the README when converting.
- Once a section is fully converted, update the top-level `README.md` links from `*.ipynb` to the new path. The "Jupyter requirement" section under "Setup" can shrink considerably or be removed if no notebooks remain.
