# AI Pair Programming Documentation
## Project: Student Grade Tracker API
## Course: SDE AI — IIT Mandi (Himshikhar Program)

---

## What is AI Pair Programming?
AI pair programming means working alongside an AI assistant (Claude by Anthropic)
to write, review, and improve code — similar to how two developers would collaborate,
with one writing and the other reviewing.

---

## What Claude (AI) Generated
1. **main.py** — The complete FastAPI backend including:
   - All 4 REST endpoints (GET all, POST, GET by ID, DELETE)
   - The GPA calculation function
   - CORS middleware setup
   - Pydantic data models

2. **index.html** — The complete frontend website including:
   - Dark themed UI with CSS styling
   - JavaScript fetch calls to connect to the API
   - Add student form, search by ID, delete functionality
   - Auto GPA color coding (green/yellow/red)

3. **test_main.py** — All 5 test cases including:
   - Test for adding a student
   - Test for getting all students
   - Test for getting a student by ID
   - Test for 404 not found error
   - Test for deleting a student

---

## What I (Ankith) Did
1. **Set up the environment** — Installed Python, FastAPI, uvicorn, pytest
2. **Reviewed all the code** — Read through every file to understand what it does
3. **Ran and tested the application** — Started the server, opened the browser,
   manually tested adding/deleting students
4. **Debugged a real issue** — The uvicorn command didn't work in PowerShell,
   I identified the fix: using `python -m uvicorn` instead
5. **Verified all tests passed** — Ran pytest and confirmed 5/5 tests passing
6. **Understood the architecture** — Learned how the frontend (HTML/JS) 
   communicates with the backend (FastAPI) through REST API calls

---

## Key Learnings from AI Collaboration
- AI is great at generating boilerplate and structure quickly
- Human review is essential — I had to understand each part to explain it
- The AI couldn't know my environment setup (PowerShell vs CMD issue) — 
  that required human debugging
- AI pair programming speeds up development but the developer must 
  understand the output

---

## Technologies Used
- **Python 3.14** — Backend language
- **FastAPI** — REST API framework
- **Uvicorn** — ASGI server to run the API
- **Pytest** — Testing framework
- **HTML/CSS/JavaScript** — Frontend website
- **Claude (Anthropic)** — AI pair programming assistant