# Introduction

This examples builds on the concepts shown in [Serve index and RAG pipelines over HTTP using Flask](/langchain/RAG-serve/README.md)

We'll take the Python REST API and add it to a Docker container. Then we'll test the deployment in the same way we did previously to show the behavior is still the same.

 ![Docker Containers](/images/docker-container.png?raw=true "Docker Containers")

Solution Components used
 - Prompt Template: based on https://smith.langchain.com/hub/rlm/rag-prompt
 - Embedding Model: OpenAI Embeddings, remote access (Requires paid account)
 - Large Language Model: OpenAI Chat, gpt-3.5-turbo-0125, remote access (Requires paid account)
 - Vectorstore: Chroma, local instance (Open source)
 - Web Framework: Flask
 - Container: Docker
 - Container Monitoring: Docker CLI, Docker Desktop

Paid model access should cost a few cents of usage fees.

# Concepts

## Containers

A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another.

One standard for containers is the open source Docker container. A Docker container consists of a plain text Docker file with the name `Dockerfile` (no extension) that can be built to form a binary file. That binary software unit is called an image and when the image is run alongside storage and networking it is called a container or container instance. 

## Dockerfile format

Docker files provide the steps to build a docker image. We'll use a few different instructions for our example. A full reference of possible commands in a Docker file can be found here: https://docs.docker.com/reference/dockerfile/ 

### Base image

The base image is defined using the `FROM` statement. The base image references an existing container from a container registry, such as the Docker Hub website or a private container registry. We'll use the `latest` tag for the official Python image. We might also consider using a specific version tag to make sure the software in out container has exactly the version of Python we know works.

```dockerfile
FROM python:latest
```

### Working directory

The `WORKDIR` command sets the working directory in the container for all commands that follow. This allows us to shorten the number of commands needed to build the image. Setting the working directory also has the side effect of creating the directory if it doesn't already exist.

```dockerfile
FROM python:latest
```

### Copy files

The `COPY` command moves files from the host to the container.

```dockerfile
COPY app.py /app
COPY custom_pipelines.py /app
COPY requirements.txt /app
```

### Run commands

The `RUN` command can be used to run arbitrary commands in the container. In this case we use run commands to install our app's dependencies using `pip`

```dockerfile
RUN pip install chromadb
RUN pip install -r requirements.txt
```

### Change users

Containers are not a strong isolation boundary in the sense that light weight containers are light weight because they rely on portions of the host operating system to run. By default Docker files are run as root. We can create a user and change to that user context by adding additional commands

```dockerfile
RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser
USER appuser
```

Further reading: https://medium.com/@mccode/processes-in-containers-should-not-run-as-root-2feae3f0df3b

### Expose network ports

Containers can communicate with other containers and the host by declaring ports they intend to use. By default all ports are restricted and one must manually open ports using the `EXPOSE` command.

```dockerfile
EXPOSE 5001
```

### Start up command

The container will run a command we specify as the previously set user from the current container working directory. In our case we wank to run our Flask app with a specific host address and port to listen on.

```dockerfile
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5001"]
```

### Full implementation

The full docker file with all of our commands is listed below for reference.

```dockerfile
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
```

## Build a container

Containers are built by executing each command and generating a final binary image that is identified by a name and tag. Each command generates a layer identified by a unique hash. This allows the docker engine to cache intermediate layers that haven't changed since the last build. Tags act as aliases where they refer to same hash which allows image repositories to avoid storing duplicates of the same binary content.

## Run a container

Docker includes mechanism to run a single container or a composition of containers through Docker Compose. Other technologies such as Kubernetes allow complex container arrangements to run in unison with additional features such as auto scaling, health monitoring and high availability compute.

When a container is run, other important options can be specified such as

- Attached storage
- Networking
- Environment variables
- CPU and memory limits

## Container registry

An online collection of container images that supports the Docker Hub protocols is called a container registry. Content on Docker Hub is public without a private subscription. Various cloud providers offer private instances of container registries.

Examples: 
- https://hub.docker.com
- https://azure.microsoft.com/en-us/products/container-registry
- https://aws.amazon.com/ecr/
- https://cloud.google.com/artifact-registry

# Dependencies

All of the dependencies listed below need to be in place before running the code.

 - Funded OpenAI account
 - Docker installed
 - Sufficient storage

## OpenAI Account

You'll need an OpenAI developer account an API Key. You will also need to purchase credits before making calls to the embedding model.

## Docker installed

Docker must be installed on the machine making the build and running the container. Docker Desktop is free for small businesses. The open source Docker command is also available for free as a separate download.

## Sufficient storage

While Docker images are smaller that full virtual machine operating systems, images and layers can still get very large, into the GB range. While you develop with Docker containers you may want to clean up periodically because abandoned experiments can accumulate to be 30 or 40 GB after an active debug session.

# Running the example

## Build the container

1. Change to the docker-serve directory

`cd <ml-reference-designs/langchain/docker-serve>`

2. Build and tag the docker image

`docker build -t rag-serve .` 

This command will name the image `rag-serve` and give it the default tag of latest. This command is equivalent to `docker build -t rag-serve:latest .` The dot(`.`) in the command tell the build command to look for the `Dockerfile` definition in the current directory.

## Run the container

 `docker run --name rag-serve -p 5001:5001 -e OPENAI_API_KEY=<your key> -d rag-serve`

 This command runs a container
 - With a friendly name of `rag-serve`
 - Binds the container port `5001` to the host port of `5001`. The port mapping has the format `container:host`
 - The `OPENAI_API_KEY` environment variable is populated with your OpenAI account's key value
 - The container starts as a background daemon where the command completes, the container keeps running in the background and returns immediately to the shell prompt.

 ## Confirm the container is running

 The Docker Desktop tool will show running containers. The command line can also be used to run the `docker ps` command. This command will return output similar to the following:

 ```
docker ps
CONTAINER ID   IMAGE       COMMAND                  CREATED       STATUS       PORTS                    NAMES
59865e8eec8f   rag-serve   "flask run --host 0.…"   4 hours ago   Up 4 hours   0.0.0.0:5001->5001/tcp   rag-serve

 ```

 ## Test the container

 The containerized version should behave exactly the same as the stand alone build referenced in the introduction. The same exact `curl` commands can be used to test the language chain inside the container.

## End the container

The container can be stopped at anytime by passing the image name to the `docker kill` command. For our example the command would be `docker kill rag-serve`
