# App1 Microservice

This is the `app1` microservice, responsible for handling user-related features. It utilizes the shared components from the `core_project`.

## Features

-   Provides an API endpoint to list all users.
-   Integrates the shared health check endpoint.

## Setup and Running

There are two primary ways to run this project: locally with a Python virtual environment or with Docker (recommended).

### Prerequisites

-   Git
-   Python 3.9+
-   Docker & Docker Compose
-   A running SSH agent with your GitHub SSH key added (`ssh-add`)

### Method 1: Running with Docker Compose (Recommended)

This is the easiest way to get started. The configuration is defined in the `docker-compose.yml` file in the project's root directory.

1.  **Navigate to the project root:**
    ```bash
    cd /home/gopesh/projects/tmp
    ```

2.  **Build the service image:**
    This command builds the Docker image for `app1`, securely accessing the `core_project` from your Git repository using your local SSH agent.
    ```bash
    docker-compose build app1
    ```

3.  **Start the service:**
    ```bash
    docker-compose up app1
    ```

    The service will be available at `http://localhost:8001`.

### Method 2: Running with Docker Manually

1.  **Navigate to the app directory:**
    ```bash
    cd /home/gopesh/projects/tmp/app1
    ```

2.  **Build the Docker image:**
    ```bash
    DOCKER_BUILDKIT=1 docker build --ssh default -t app1 .
    ```

3.  **Run the Docker container:**
    ```bash
    docker run --rm -p 8001:8000 --name app1_container app1
    ```

### Method 3: Running Locally (for Development)

This method uses your local Python environment and installs the `core_project` from the local file system.

1.  **Navigate to the app directory:**
    ```bash
    cd /home/gopesh/projects/tmp/app1
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    The `requirements.txt` is configured to install the shared packages from the adjacent `core_project` directory.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Start the development server:**
    ```bash
    python manage.py runserver 8001
    ```

## API Endpoints

-   **List Users**: `GET http://localhost:8001/users/`
-   **Health Check**: `GET http://localhost:8001/core/health/`