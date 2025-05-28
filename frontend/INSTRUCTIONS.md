TimeTrackr
A web application for tracking time expenses with project categorization and passive LLM summaries.
Prerequisites

Docker and Docker Compose
Python 3.12
Node.js (optional for local frontend development)
Render account (free tier)
External LLM API URL and key

Local Setup

Clone the repository:git clone <your-repo-url>
cd timetrackr


Set up environment variables:Create a .env file in the root directory:DATABASE_URL=postgresql://timetrackr:timetrackr@localhost:5432/timetrackr
JWT_SECRET=your-secret-key-change-this
LLM_API_URL=http://external-llm-api.com/summary
LLM_API_KEY=your-llm-api-key


Run with Docker Compose:docker-compose up --build


Access the app:
Backend: http://localhost:8000/docs (Swagger UI)
Frontend: Open frontend/index.html or run npm start in frontend/



Deploy to Render

Create a Render account and set up a new Web Service and PostgreSQL database.
Push to GitHub:git init
git add .
git commit -m "Initial commit"
git remote add origin <your-github-repo-url>
git push origin main


Configure Render:
Web Service:
Repository: Your GitHub repo
Build Command: pip install -r requirements.txt
Start Command: uvicorn app.main:app --host 0.0.0.0 --port 80
Environment Variables: Copy from .env


Database: Note the internal DATABASE_URL provided by Render.


Deploy: Trigger deployment in Render’s dashboard.

Usage

Register/login via the frontend.
Create categories and projects.
Log time entries with hours and descriptions.
Fetch LLM summaries (assumes external API).
View time spent by category.

Scaling

Free Tier: Render’s free tier supports personal use (web service and PostgreSQL).
Paid Tier: Upgrade to Starter ($7/month) or Standard ($25/month) for production.
Database: Render’s free PostgreSQL expires after 90 days; upgrade to persistent storage ($7/month).

Notes

Replace LLM_API_URL and LLM_API_KEY with actual values from your external LLM API.
Ensure the frontend is hosted separately (e.g., Netlify) for production.

