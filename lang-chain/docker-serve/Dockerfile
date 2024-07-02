FROM python:latest

WORKDIR /app
COPY app.py /app
COPY custom_pipelines.py /app
COPY requirements.txt /app

RUN pip install chromadb
RUN pip install -r requirements.txt

RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser
USER appuser

EXPOSE 5001
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5001"]