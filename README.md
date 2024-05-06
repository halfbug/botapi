# Bot Service README

## Overview

This bot service is developed using various Python packages to provide a robust and efficient solution. It utilizes FastAPI as the web framework for creating APIs, UVicorn for serving the FastAPI application, and several other packages for specific functionalities such as interacting with Google Cloud Storage, data manipulation with Pandas, environment variable management with Python-dotenv, and more.

## Installation

To install the required packages, you can use pip. Run the following command in your terminal:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration

Before running the service, make sure to set up the necessary configurations. Create a `.env` file in the root directory of your project and add the required environment variables. Here's an example `.env` file:

```dotenv
# Example .env file

API_V1_ROUTE="/api/v1"
ENV_STATE=dev
DATABASE_URL="postgresql"
DEV_API_V1_ROUTE="/api/v1"
GOOGLE_API_KEY="KGLKERLK"
GOOGLE_CSE_ID="1"
OPENAI_API_KEY

# Other environment variables...
```

## Usage

To run the bot service, execute the following command:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
.venv\Scripts\activate
python -m uvicorn app.main:app --reload
```

This will start the FastAPI application and make it available on `http://localhost:8000`.

## Packages Used

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- [UVicorn](https://www.uvicorn.org/): A lightning-fast ASGI server, built on uvloop and httptools, for running asynchronous Python web code.
- [Google Cloud Storage](https://cloud.google.com/storage): A fully-managed, highly-durable, and highly available object storage service.
- [Pydantic](https://pydantic-docs.helpmanual.io/): Data validation and settings management using Python type annotations.
- [Pandas](https://pandas.pydata.org/): A fast, powerful, flexible, and easy-to-use open-source data manipulation and analysis library.
- [Python-dotenv](https://pypi.org/project/python-dotenv/): Reads the key-value pair from `.env` file and adds them to environment variable.
- [Pydantic-settings](https://pypi.org/project/pydantic-settings/): A lightweight settings management library built on top of Pydantic.
- [OpenAI](https://openai.com/): A leading AI research lab providing state-of-the-art natural language processing models.
- [Langchain](https://github.com/ACollectionOfAtoms/langchain): A Python library for creating a chain of language models.
- [Langchain-openai](https://github.com/ACollectionOfAtoms/langchain-openai): A plugin for Langchain library to use OpenAI language models.
- [Chromadb](https://github.com/ACollectionOfAtoms/chromadb): A Python library for working with Chroma database.
- [Langchain_chroma](https://github.com/ACollectionOfAtoms/langchain_chroma): A plugin for Langchain library to use Chroma database.
- [Html2text](https://pypi.org/project/html2text/): A Python script that converts a page of HTML into clean, easy-to-read plain ASCII text.

## Deployment

For deploying the bot service in production, it's recommended to use a production-ready server such as Gunicorn. You can run the service using Gunicorn with the following command:

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app -b 0.0.0.0:8000
```

This command starts Gunicorn with 4 worker processes and binds it to port 8000.
