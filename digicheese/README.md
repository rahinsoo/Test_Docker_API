# FastAPI-Docker

This application is a fully containerized FastAPI application. It's an exemple of containerized api with python to manage client fidelity points of cheese factory in order to manage learning process of FastAPI and Docker to diginamic students.

## Introduction

The build start with a **Dockerfile** that defines the FastAPI application and its dependencies like **requirements.txt**. The application is built and run using **Docker Compose**, which also starts a MariaDB container as the database and an Adminer container as web database visualizer.

## Project Structure

```bash
.
├── api/                # Source code for the FastAPI application
│   ├── main.py         # Entry point for the FastAPI app
│   ├── database.py     # Database connection setup
│   ├── models/         # SQLAlchemy models
│   ├── repositories/   # Data access layer
│   ├── services/       # Business logic layer
│   ├── routers/        # API route definitions
│   └── schemas/        # Pydantic schemas for data validation
│
├── tests/              # Test suite for the application
│   ├── __init__.py     # Required for pytest to discover the tests
│   ├── conftest.py     # Pytest configuration and fixtures
│   └── test_client.py  # Integration tests for the client routes
│
├── .gitignore          # Files and directories to ignore in Git
├── Dockerfile          # Dockerfile to build the FastAPI app
├── docker-compose.yml  # Docker Compose configuration
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (e.g., database credentials)
├── .env.example        # Example .env file with environment variables
├── README.md           # Project documentation
└── test.db             # SQLite database for testing (auto-generated with tests)
```

## Prerequisites

Ensure the following tools are installed on your system:

- **Docker**: [Installation Guide](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Installation Guide](https://docs.docker.com/compose/install/)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/robinhotton/Projet-FastAPI-Docker.git # Private repository
cd Projet-FastAPI-Docker
```

### 2. Configure Environment Variables

Create a `.env` file in the project root and define the variables.  
You can use the `.env.example` file as a template.  

### 3. Build and Run the Application

To build the Docker image and start all services (FastAPI and MariaDB):

```bash
docker-compose up --build
```

Once running, the application will be accessible at:  
**[http://localhost:8000](http://localhost:8000)**

The automatically generated API documentation will be available at:

- Swagger UI: **[http://localhost:8000/docs](http://localhost:8000/docs)**
- ReDoc: **[http://localhost:8000/redoc](http://localhost:8000/redoc)**

### 4. Stop the Application

To stop and remove all containers:

```bash
# -v flag removes the volumes
docker-compose down -v
```

## Database Management

MariaDB is included as part of the `docker-compose.yml` file. You can interact with the database using any MySQL/MariaDB client or using adminer, a lightweight database management tool like phpMyAdmin.

### Access the Database via Adminer

Adminer is a lightweight database management tool that is accessible via a web browser.

Navigate to **[http://localhost:8070](http://localhost:8070)** and use the following credentials:

- **System**: MySQL/MariaDB
- **Server**: db
- **Username**: admin
- **Password**: Admin123!
- **Database**: digicheese

Dont forget to replace `username`, `password`, and `database` with the values defined in your `.env` file.

### Access the Database via other Tools

You can also connect to the MariaDB database using any MySQL client (like MySQL Workbench, DBeaver, etc.) with the following connection details:

The other connection details are the same as for Adminer :
- **Port**: 3307 (or the port defined in your `.env` file in `PORT_DB_VISUALISATION`)

### Access the MariaDB Container

To open a MariaDB shell inside the container:

```bash
docker-compose exec db mysql -u root -p
```

Use the password defined in your `.env` file with `MYSQL_ROOT_PASSWORD`.

## Running Tests

### Option 1: Run Tests in a Dedicated Test Container

Run the tests directly in a disposable container:

```bash
docker-compose run --rm fastapi pytest
```

### Option 2: Run Tests Inside the FastAPI Container

Access the FastAPI container shell and run the tests manually:

```bash
docker-compose exec fastapi bash
pytest
```

## Debugging

### Access the FastAPI Container Shell

To access the FastAPI container for debugging:

```bash
docker-compose exec fastapi bash
```

### View Container Logs

Check logs for the FastAPI or MariaDB containers:

```bash
docker-compose logs fastapi
docker-compose logs db
```
