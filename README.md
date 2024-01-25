# ToDo Application

## Introduction
This is a ToDo application built using Django framework. It allows users to create, manage, and track their tasks efficiently.

## Features
- Create and manage tasks
- Mark/Un-mark tasks as completed
- User authentication and authorization

## Getting Started
To get started with the ToDo application, follow the steps below in command line:

### Installation
1. Clone the repository: `git clone https://github.com/renuka010/TodoApp.git`
2. Activate the virtual environment:
    - For Windows: `venv\Scripts\activate`
    - For macOS/Linux: `source venv/bin/activate`
3. Change to the project directory: `cd todo`
4. Install the required packages: `pip install -r requirements.txt`

### Usage 
1. Build the Docker image: `docker-compose build`
2. Run the Docker image: `docker-compose up`
3. Access the application in your browser at `http://localhost:8000`

## Running without Docker
To run the ToDo application in your local machine without Docker, follow the steps below:

1. Run the Django development server: `python manage.py runserver`
2. Access the application in your browser at `http://localhost:8000`

## Screenshots
![App screenshot](/todo/static/images/todo.png)
