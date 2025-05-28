from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import TimeEntry, Project, Category
from app.schemas import TimeEntryCreate, TimeEntryOut, CategorySummary
from app.dependencies import get_db, get_current_user

router = APIRouter()

@router.post("/", response_model=TimeEntryOut)
def create_time_entry(entry: TimeEntryCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    project = db.query(Project).filter(Project.id == entry.project_id, Project.user_id == user.id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found or not owned by user")
    db_entry = TimeEntry(**entry.dict(), user_id=user.id)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@router.get("/", response_model=list[TimeEntryOut])
def read_time_entries(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(TimeEntry).filter(TimeEntry.user_id == user.id).all()

@router.get("/summary", response_model=list[CategorySummary])
def get_category_summary(db: Session = Depends(get_db), user=Depends(get_current_user)):
    summary = (
        db.query(
            Category.id.label("category_id"),
            Category.name.label("category_name"),
            func.sum(TimeEntry.hours).label("total_hours")
        )
        .join(Project, Project.category_id == Category.id)
        .join(TimeEntry, TimeEntry.project_id == Project.id)
        .filter(Project.user_id == user.id)
        .group_by(Category.id, Category.name)
        .all()
    )
    return [CategorySummary(category_id=row.category_id, category_name=row.category_name, total_hours=row.total_hours) for row in summary]