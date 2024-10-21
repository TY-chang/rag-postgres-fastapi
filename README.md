# Simple RAG (Retrieval-Augmented Generation) Project

## Introduction
This repository implements a basic Retrieval-Augmented Generation (RAG) system, relying on the following technologies:
- **FastAPI**: For creating the API endpoints.
- **Alembic**: For managing database migrations.
- **PostgreSQL**: As the database, with the **pgvector** extension for handling vectorized data.

## Environment Setup
### Poetry
This project uses Poetry for dependency management.

1. Install Poetry if not already installed:
    ```bash
    pip install poetry
    ```

2. Install dependencies:
    ```bash
    poetry install
    ```

### Environment Variables
1. Copy the environment template to create your `.env` file:
    ```bash
    cp .template.env .env
    ```

2. Edit the `.env` file to include your OpenAI API key and the PostgreSQL DSN (Data Source Name). Example:
    ```
    OPENAI_API_KEY=sk-...
    DB_DSN=postgresql://user:password@localhost:5432/rag_db
    ```

## Running the Application

### Local Development
To run the application locally using Poetry, use the following command:
```bash
poetry run uvicorn interface.http_server:app --host 0.0.0.0 --port 80
```
## Docker Setup
The repository is Dockerized to simplify deployment and testing.

1. **Build the Docker containers**:
    Use the `just` command to build the Docker containers.
    ```bash
    just build
    ```

2. **Run the Docker containers**:
    Start the Docker containers in detached mode:
    ```bash
    just up
    ```

3. **Access the API**:
    Once the containers are up and running, the API will be available at:
    ```
    http://localhost:80
    ```

4. **Load Knowledge Base**:
    You can load your knowledge base from a CSV file. Replace `<filename>` with the path to your CSV file.
    ```bash
    just load_knowledge filename="<filename>"
    ```

## Database Migrations
Alembic is used for managing database migrations. The following commands help manage migrations:

1. **Create a new migration** (replace `<message>` with your migration message):
    ```bash
    just make_migration message="<message>"
    ```

2. **Apply all pending migrations**:
    ```bash
    just migrate
    ```

3. **Rollback the last migration**:
    ```bash
    just downone
    ```

## Loading Knowledge Base
To load the knowledge base data from a CSV file into the database, use the following command. Replace `<filename>` with the path to your CSV file:
```bash
just load_knowledge filename="<filename>"
```

## Test
