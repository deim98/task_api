# Task and User Management API
A simple RESTful API for managing tasks and users, built with Flask and Flask-RESTx. This project includes two microservices: Task and User, each with its own routes and database schema. The project also uses MongoDB as a backend database.

# Features
- CRUD operations for managing tasks and users
- JWT-based authentication
- MongoDB integration for data storage
- RESTful API with Swagger documentation available at /docs
- Dockerized setup for easy deployment
# Table of Contents
1. Project Structure
2. Setup Instructions
3. Running the Application
4. API Endpoints
5. Project Structure

# The project is organized as follows:

bash
Copy code
task_user_api/
│
├── config.py                 # Configuration settings (MongoDB URI, JWT secret)
├── main.py                   # Main application entry point
├── docker-compose.yml        # Docker Compose file
├── task_service/
│   ├── models/
│   │   └── task_model.py     # Task model definition
│   ├── routes/
│   │   └── task_routes.py    # Task routes
│   └── schemas/
│       └── task_schema.py    # Marshmallow schema for task validation
│
└── user_service/
    ├── models/
    │   └── user_model.py     # User model definition
    ├── routes/
    │   └── user_routes.py    # User routes
    └── schemas/
        └── user_schema.py    # Marshmallow schema for user validation
# Setup Instructions
# Prerequisites
- Python 3.8+
- Docker and Docker Compose
- MongoDB (if not using Docker)
- Installation
- Clone this repository:

- bash
- Copy code
`git clone <repository_url>`
 `cd task_user_api `
- Create a virtual environment:

- bash
- Copy code
`python -m venv venv`
 `source venv/bin/activate`  # On Windows use `venv\Scripts\activate`
# Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables in a .env file for MongoDB URI and JWT secrets:

# makefile
Copy code
MONGO_URI=mongodb://mongo:27017/<your_database>
JWT_SECRET_KEY=your_secret_key
Docker Setup
To run the entire application (Task and User services, along with MongoDB) with Docker, use:

bash
Copy code
docker-compose up --build
This will spin up the Task and User services on ports 5000 and 5001 respectively, and MongoDB on port 27017.

# Running the Application
Without Docker
Run the application locally by running:

bash
Copy code
python main.py
Access the application at http://127.0.0.1:5000.

# With Docker
If running with Docker Compose, access the services at:

Task service: http://127.0.0.1:5000/tasks
User service: http://127.0.0.1:5000/users
Swagger Documentation: http://127.0.0.1:5000/docs
API Endpoints
Task Endpoints
GET /tasks - Retrieve all tasks
POST /tasks - Create a new task
GET /tasks/<id> - Retrieve a specific task by ID
PATCH /tasks/<id> - Update a specific task
User Endpoints
GET /users - Retrieve all users
POST /users - Create a new user
GET /users/<id>/tasks - Retrieve tasks assigned to a specific user
Environment Variables
MONGO_URI: MongoDB URI, including database name
JWT_SECRET_KEY: Secret key for JWT authentication
Notes
Ensure MongoDB is running or accessible at the specified URI.
Default API documentation is available at /docs.
