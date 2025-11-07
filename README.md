🧮 Module 12: User & Calculation Routes + Integration Testing
👤 Author

Muhammad Arham
GitHub Repository: https://github.com/arhamidrees63/assignment12
Docker Hub:
🔗 https://hub.docker.com/r/arhamidrees63/module12

🚀 Objective

This project implements a complete FastAPI backend featuring:

Secure User Registration and Login with password hashing and JWT tokens

Full Calculation CRUD (BREAD) operations

Comprehensive Integration & Unit Tests using pytest

Automated CI/CD Pipeline via GitHub Actions and Docker Hub deployment

🧰 Tech Stack
Component	Description
FastAPI	Modern Python web framework for async APIs
PostgreSQL	Relational database used for persistence
SQLAlchemy	ORM for models and database management
Pydantic v2	Schema validation and type safety
Pytest + Coverage	Automated testing framework
Docker & Docker Hub	Containerization and image hosting
GitHub Actions	Continuous Integration / Continuous Deployment
⚙️ Setup Instructions (Local Development)
1️⃣ Clone the Repository
git clone git@github.com:arhamidrees63/assignment12.git
cd assignment12

2️⃣ Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
uvicorn app.main:app --reload

5️⃣ Access the API Docs

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

🧪 Running Tests
Run All Tests
pytest --maxfail=1 -v --cov=app --cov-report=term-missing


✅ Example output:

===================== 101 passed, 1 skipped =====================
---------- coverage: platform linux, python 3.12 -----------
TOTAL                          649    165    75%

Test Highlights

/users/register → User creation with password validation

/users/login → JWT authentication

/calculations → Add, Retrieve, Edit, Delete operations

Integration tests confirm schema and database behavior

🧩 API Endpoints Overview
👥 User Routes
Method	Endpoint	Description
POST	/users/register	Register a new user
POST	/users/login	Login and generate access token
🧮 Calculation Routes
Method	Endpoint	Description
GET	/calculations	Browse all calculations
GET	/calculations/{id}	Retrieve a specific calculation
POST	/calculations	Add a new calculation
PUT / PATCH	/calculations/{id}	Edit or update a calculation
DELETE	/calculations/{id}	Delete a calculation
🧱 Database (PostgreSQL)

Local .env or config example:

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=fastapi_db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432


To start the database (optional for manual testing):

docker compose up -d

🐳 Docker Deployment
🧩 Image Details

Docker Hub:
🔗 https://hub.docker.com/r/arhamidrees63/module12

Build the Docker Image
docker build -t arhamidrees63/module12:latest .

Run the Container Locally
docker run -d -p 8000:8000 arhamidrees63/module12:latest


Now open:
👉 http://localhost:8000/docs

Pull from Docker Hub (any system)

To run directly from Docker Hub:

docker pull arhamidrees63/module12:latest
docker run -d -p 8000:8000 arhamidrees63/module12:latest

⚙️ GitHub Actions CI/CD

Each push triggers:

Build the Docker image

Run all integration + unit tests

Push to Docker Hub on successful test completion

Example Workflow File (.github/workflows/ci.yml)
name: CI Pipeline

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:14
        env:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: fastapi_db
        ports: ['5432:5432']
        options: >-
          --health-cmd="pg_isready -U postgres"
          --health-interval=5s
          --health-timeout=5s
          --health-retries=5

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: 3.12

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run Tests
        run: pytest --maxfail=1 -v --cov=app --cov-report=term-missing

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build Docker Image
        run: docker build -t arhamidrees63/module12:latest .
      - name: Log in to Docker Hub
        run: echo "${{ secrets.DOCKER_HUB_TOKEN }}" | docker login -u "arhamidrees63" --password-stdin
      - name: Push to Docker Hub
        run: docker push arhamidrees63/module12:latest

🧠 Reflection

This module was my first full-stack backend integration combining authentication, CRUD operations, and CI/CD. I learned how to structure scalable APIs, validate data using Pydantic, and verify features through comprehensive testing. Automating builds and Docker deployments with GitHub Actions streamlined my development workflow and gave me hands-on experience in real-world DevOps practices.