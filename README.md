# 🚀 FastAPI RESTful API Example

This project is a Python-based RESTful API built using **FastAPI**, a modern web framework designed for speed, efficiency, and developer productivity.

FastAPI uses **Python type hints** and **Pydantic** for data validation, serialization, and documentation generation via **OpenAPI** (Swagger UI). The app is asynchronous and designed to run with **Uvicorn** or **Gunicorn**.

---

## 📌 Features

- ⚡ High-performance API with [FastAPI](https://fastapi.tiangolo.com/)
- 📄 Auto-generated OpenAPI (Swagger) docs
- ✅ Input validation with [Pydantic](https://docs.pydantic.dev/)
- 🔄 Asynchronous support using `async/await`
- 🧪 Easy-to-test modular structure
- 🚀 Production-ready using Uvicorn/Gunicorn

---

## 🧰 Tech Stack

| Layer         | Tooling                           |
|---------------|-----------------------------------|
| Web Framework | [FastAPI](https://fastapi.tiangolo.com/) |
| Data Models   | [Pydantic](https://docs.pydantic.dev/) |
| Server        | [Uvicorn](https://www.uvicorn.org/) / [Gunicorn](https://gunicorn.org/) |
| Language      | Python 3.10+                      |

---

## 📦 Installation

1. **Clone the repository**
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```bash
pip install -r requirements.txt
pip install fastapi uvicorn
```
## 🚀 Running the App

```bash
git clone https://github.com/yourusername/fastapi-rest-api.git
cd fastapi-rest-api
uvicorn app.main:app --reload
