# Smart Task Manager REST API

A well-structured Task Management REST API built using FastAPI and MySQL.
This project demonstrates clean backend architecture, validation, filtering, pagination, and proper error handling.

---

## Features

* Create a new task
* Get all tasks with:
  * filtering (status)
  * search (title)
  * pagination
  * sorting
* Update task status with controlled transitions
* Delete tasks safely
* Input validation using Pydantic
* Global error handling
* Clean and consistent API responses

---

## Tech Stack

* Python
* FastAPI
* MySQL
* SQLAlchemy (ORM)
* Pydantic
* Uvicorn

---

## Project Structure

```
task-manager-api/
│
├── app/
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   ├── controllers/
│   ├── database/
│
├── requirements.txt
├── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Setup MySQL Database

```
CREATE DATABASE task_manager;
```

### 5. Configure Database Connection

Update in `connection.py`:

```
mysql+pymysql://username:password@localhost/task_manager
```

### 6. Run Server

```
uvicorn app.main:app --reload
```

---

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Endpoint           | Description                               |
| ------ | ------------------ | ----------------------------------------- |
| POST   | /tasks             | Create task                               |
| GET    | /tasks             | Get tasks (filter/search/pagination/sort) |
| PATCH  | /tasks/{id}/status | Update task status                        |
| DELETE | /tasks/{id}        | Delete task                               |

---

## Example Query

```
GET /tasks?status=pending&search=learn&page=1&limit=5&sort=desc
```

---

## Database Schema

```
tasks (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  status ENUM('pending','in_progress','completed') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

---

## Deliverables

* GitHub Repository
* README
* Postman Collection
* Database Schema

---

## Highlights

* Clean layered architecture (routes, controllers, models)
* Smart filtering, pagination, and sorting
* Strong validation and error handling
* Production-style API design

---
