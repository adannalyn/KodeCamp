# KodeCamp To-Do API

A RESTful To-Do application built with **FastAPI** and **Pydantic** as part of the KodeCamp program. The API provides full CRUD functionality for managing tasks with status tracking.

---

## Features

- Create, read, update, and delete to-do items
- Status tracking with three states: `pending`, `in-progress`, `completed`
- Input validation using Pydantic models
- Auto-incrementing task IDs
- Interactive API documentation (Swagger UI)

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Framework | FastAPI |
| Validation | Pydantic |
| Server | Uvicorn |
| Language | Python 3.12+ |

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/todos` | Retrieve all to-do items |
| `GET` | `/todos/{id}` | Retrieve a single to-do item by ID |
| `POST` | `/todos` | Create a new to-do item |
| `PUT` | `/todos/{id}` | Update an existing to-do item |
| `DELETE` | `/todos/{id}` | Delete a to-do item |

---

## Request and Response Format

### Create / Update a To-Do

```json
{
  "id": 0,
  "title": "Complete KodeCamp assignment",
  "description": "Build a REST API with FastAPI",
  "status": "pending"
}
```

**Status options:** `pending`, `in-progress`, `completed`

---

## Installation

Clone the repository:

```bash
git clone https://github.com/adannalyn/KodeCamp.git
cd KodeCamp
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the development server:

```bash
uvicorn todo:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

Access the interactive documentation at `http://127.0.0.1:8000/docs`.

---

## Project Structure

```
KodeCamp/
├── todo.py             # Main application with routes and models
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

---

## Notes

- Data is stored in memory and resets when the server restarts.
- Built as a learning project for the KodeCamp backend development track.
- The `id` field in the request body is auto-assigned by the server; any value sent by the client is overwritten.