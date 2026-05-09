# Dependencies

You will need all of the following dependencies to run this example:

 - OpenAI token
 - Python virtual environment

## Hugging Face token

Log in to OpenAI and generate an API key.

Create an environment file named `.env`. Add the following line to your environment file:

```ini
OPENAI_API_KEY=<your key>
```

## Python Virtual Environment

Set up a Python virtual environment ([instructions](../../docs/setup/python-venv.md)), then install this example's dependencies with `pip install -r requirements.txt`.

# Running the code

```
python app.py
Question:  What are some shape namees in geometry?
Answer:  Some shape names in geometry include circle, triangle, square, rectangle, pentagon, hexagon, octagon, and sphere.
```