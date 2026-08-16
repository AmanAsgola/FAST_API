# FastAPI Practice 🚀

A collection of hands-on exercises and mini-projects while learning **FastAPI** — a modern, high-performance Python web framework for building APIs.

## 📌 About This Repository

This repo documents my journey learning FastAPI. It contains code snippets, small projects, and experiments built while exploring different parts of the framework. I'll keep updating it as I continue practicing.

## 🧠 Topics Covered

- [x] Basic routing (GET, POST, PUT, DELETE)
- [x] Path & query parameters
- [x] Request body validation with Pydantic models
- [ ] Response models & status codes
- [ ] Dependency Injection
- [ ] Error handling & custom exceptions
- [ ] Middleware
- [ ] Database integration (SQLAlchemy / SQLModel)
- [ ] Authentication & Authorization (OAuth2, JWT)
- [ ] File uploads
- [ ] Background tasks
- [ ] Testing with pytest & TestClient
- [ ] Auto-generated docs (Swagger UI / ReDoc)

> Check items off as you cover them so the README tracks your progress.

## 🛠️ Tech Stack

- **Python** 3.x
- **FastAPI**
- **Uvicorn** (ASGI server)
- **Pydantic**
- *(add anything else you're using — SQLAlchemy, PostgreSQL, Docker, etc.)*

## 📂 Project Structure

```
fastapi-practice/
├── app/
│   ├── main.py
│   ├── models/
│   ├── routers/
│   └── schemas/
├── requirements.txt
└── README.md
```
*(update this to match your actual folder layout)*

## ⚙️ Installation & Setup

1. Clone the repository
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app
   ```bash
   uvicorn app.main:app --reload
   ```

5. Open in your browser
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

## 🚧 Future Plans

- Build small real-world APIs (To-Do app, Blog API, Auth system)
- Explore async database operations
- Add Docker support
- Write more tests

## 🤝 Contributing

This is a personal learning repo, but feedback and suggestions are always welcome.

## 📄 License

Open source under the [MIT License](LICENSE).

---

⭐ If this helps your own FastAPI learning journey, feel free to star the repo!
