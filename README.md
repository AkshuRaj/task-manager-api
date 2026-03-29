# Task Manager REST API

> A production-ready task management system built with modern Python web technologies. Designed with clean architecture principles, robust authentication, and comprehensive data validation.

## What's Inside

- **Secure Authentication** – User registration and JWT-based login with token expiration
- **CRUD Operations** – Create, read, update, and delete tasks with full control
- **Smart Filtering** – Filter tasks by status, search by title, with pagination support
- **Input Validation** – Comprehensive data validation for usernames and passwords using Pydantic
- **Password Security** – Argon2 hashing for secure password storage (industry standard)
- **Protected Endpoints** – Bearer token authentication for all protected routes
- **Modern Architecture** – Layered design with controllers, routes, schemas, and models

---

## Technology Stack

**Backend Framework**
- **FastAPI** – Modern, fast Python web framework with automatic API documentation
- **Uvicorn** – Lightning-fast ASGI server for production deployment

**Database & ORM**
- **MySQL** – Reliable relational database
- **SQLAlchemy** – Powerful ORM for database operations

**Security & Authentication**
- **python-jose** – JWT (JSON Web Token) creation and validation
- **Argon2-cffi** – State-of-the-art password hashing algorithm
- **passlib** – Password utilities library

**Data Validation**
- **Pydantic** – Runtime data validation and serialization

---

## Project Architecture

```
task-manager-api/
│
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── models/                 # SQLAlchemy ORM models
│   │   ├── task.py             # Task model schema
│   │   └── user.py             # User model schema
│   ├── schemas/                # Pydantic validation schemas
│   │   ├── task_schema.py      # Task request/response schemas
│   │   └── auth_schema.py      # Auth request/response schemas
│   ├── routes/                 # API route handlers
│   │   ├── task_routes.py      # Task endpoints
│   │   └── auth_routes.py      # Authentication endpoints
│   ├── controllers/            # Business logic layer
│   │   └── task_controller.py  # Task operations logic
│   ├── database/               # Database configuration
│   │   └── connection.py       # SQLAlchemy setup & session
│   └── utils/                  # Helper utilities
│       ├── auth.py             # Token & password utilities
│       └── dependency.py       # JWT dependency injection
│
├── requirements.txt            # Python dependencies
├── schema.sql                  # Database schema
├── Task-Manager-Collection.json # Postman collection
└── README.md                   # Project documentation
```

**Architecture Highlights:**
- **Separation of Concerns** – Each layer has a specific responsibility (routes → controllers → models)
- **Dependency Injection** – FastAPI's `Depends` for clean, testable code
- **Schema Validation** – Pydantic ensures data integrity at entry points

---

## Getting Started

### Prerequisites
- Python 3.8+
- MySQL 5.7+
- pip (Python package manager)

### Installation

**1. Clone the Repository**
```bash
git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api
```

**2. Create Virtual Environment**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure Database**

Create a MySQL database:
```sql
CREATE DATABASE task_manager;
```

Update the database connection string in `app/database/connection.py`:
```python
DATABASE_URL = "mysql+pymysql://username:password@localhost:3306/task_manager"
```

**5. Start the Server**
```bash
uvicorn app.main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

### Interactive API Documentation

Once the server is running, access the auto-generated documentation:
- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

### Quick Test

Test the database connection:
```bash
curl http://127.0.0.1:8000/test-db
```

---

## Quick Start Example

**1. Sign Up a New User**
```bash
curl -X POST http://127.0.0.1:8000/signup \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "SecurePass@123"
  }'
```

**2. Login & Get Token**
```bash
curl -X POST http://127.0.0.1:8000/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "SecurePass@123"
  }'
```

**3. Create a Task**
```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project documentation",
    "description": "Write comprehensive README and API docs"
  }'
```

**4. Get All Tasks**
```bash
curl -X GET "http://127.0.0.1:8000/tasks?status=pending&sort=desc" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

Tip: Use the Postman Collection (included) for easy API testing with a UI!

---

## Authentication Flow

The API uses JWT (JSON Web Tokens) for stateless authentication. Here's how it works:

**1. User Registration**
```
POST /signup
{
  "username": "john_doe",
  "password": "SecurePass123!"
}
```

**2. User Login**
```
POST /login
{
  "username": "john_doe",
  "password": "SecurePass123!"
}
Response:
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

**3. Using the Token**
Include the token in the Authorization header for protected endpoints:
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

**4. Access Protected Resources**
All task endpoints (`/tasks`, `/tasks/{id}/status`, etc.) require valid JWT token

---

## API Reference

### Authentication Endpoints
| Method | Endpoint    | Description          | Auth Required |
|--------|-------------|----------------------|---------------|
| POST   | `/signup`   | Register new user    | No            |
| POST   | `/login`    | User login           | No            |

### Task Endpoints
| Method | Endpoint              | Description                           | Auth Required |
|--------|-----------------------|---------------------------------------|---------------|
| POST   | `/tasks`              | Create new task                       | Yes           |
| GET    | `/tasks`              | Get all tasks (with filters)          | Yes           |
| PATCH  | `/tasks/{id}/status`  | Update task status                    | Yes           |
| DELETE | `/tasks/{id}`         | Delete task                           | Yes           |

### Query Parameters (GET /tasks)
- `status` – Filter by status (pending, in_progress, completed)
- `search` – Search in task title
- `page` – Page number (default: 1)
- `limit` – Items per page (default: 5)
- `sort` – Sort order (asc, desc - default: desc for recent first)

**Example Request:**
```
GET /tasks?status=pending&search=learn&page=1&limit=5&sort=desc
```

**Example Response:**
```json
{
  "success": true,
  "count": 2,
  "data": [
    {
      "id": 1,
      "title": "Learn FastAPI",
      "description": "Build REST APIs",
      "status": "pending",
      "created_at": "2024-03-29T10:30:00"
    }
  ]
}
```

---

## Testing with Postman

A complete Postman collection is included in the repository (`Task-Manager-Collection.json`).

**How to Import:**
1. Open Postman
2. Click `Import` → Select `Task-Manager-Collection.json`
3. All endpoints will be pre-configured and ready to test
4. Update the JWT token in Authorization headers after login

This collection includes:
- User signup and login endpoints
- Task CRUD operations with pre-filled examples
- Proper authentication headers
- Sample request/response bodies

---

## Input Validation Rules

The API enforces strict validation to ensure data quality and security.

### Username Validation
- Must start with a letter (a-z, A-Z)
- Can contain letters, numbers, and underscores only
- Length: **3-20 characters**
- Example: `john_doe`, `user123` ✓

### Password Validation
- Length: **6-50 characters** (securely within Argon2 limits)
- Must contain **at least one uppercase letter** (A-Z)
- Must contain **at least one lowercase letter** (a-z)
- Must contain **at least one number** (0-9)
- Must contain **at least one special character** (@, $, !, %, *, ?, &)
- Example: `SecurePass@123` ✓

### Task Validation
- **Title**: Required, string
- **Description**: Optional, string
- **Status**: Must be one of: `pending`, `in_progress`, `completed`

---

## Key Features in Detail

### Smart Task Management
- **Filtering** – View tasks by status (pending, in_progress, completed)
- **Full-Text Search** – Search tasks by title
- **Pagination** – Handle large datasets efficiently
- **Sorting** – Sort by creation date (ascending or descending)

### Security First
- JWT tokens with expiration (2-hour default)
- Argon2 password hashing (resistant to GPU and side-channel attacks)
- Input sanitization and validation on all endpoints
- Bearer token authentication for protected routes

### Error Handling
- Comprehensive error messages for debugging
- Proper HTTP status codes
- Validation error details

---

## Roadmap & Future Enhancements

- [ ] User profiles and task ownership per user
- [ ] Role-based access control (RBAC) for admin/user roles
- [ ] Refresh token mechanism for better session management
- [ ] Task priority levels and due dates
- [ ] Email notifications for task updates
- [ ] Docker containerization for easy deployment
- [ ] Comprehensive unit and integration tests
- [ ] Rate limiting to prevent API abuse
- [ ] Activity logging and audit trails

---

## Deliverables

✓ **Source Code** – Clean, well-documented Python codebase
✓ **GitHub Repository** – Version controlled with `.gitignore`
✓ **Postman Collection** – Ready-to-use API testing (`Task-Manager-Collection.json`)
✓ **Database Schema** – Pre-configured MySQL models
✓ **Documentation** – Comprehensive README with examples
✓ **Auto-Generated Docs** – Swagger UI and ReDoc

---

## Contributing

Found a bug or have a feature idea? Feel free to open an issue or submit a pull request.

## License

This project is open source and available under the MIT License.
