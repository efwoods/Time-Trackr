from fastapi import FastAPI
from app.routers import auth, time_entries, projects, categories, llm_summaries
from app.dependencies import create_db_and_tables

app = FastAPI(title="TimeTrackr API")

# Create database tables on startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(time_entries.router, prefix="/time-entries", tags=["time-entries"])
app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(categories.router, prefix="/categories", tags=["categories"])
app.include_router(llm_summaries.router, prefix="/llm-summaries", tags=["llm-summaries"])

@app.get("/")
def read_root():
    return {"message": "Welcome to TimeTrackr"}