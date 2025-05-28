from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Project
from app.schemas import ProjectCreate, ProjectOut
from app.dependencies import get_db, get_current_user

router = APIRouter()

@router.post("/", response_model=ProjectOut)
def create_project(project: ProjectCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_project = Project(**project.dict(), user_id=user.id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@router.get("/", response_model=list[ProjectOut])
def read_projects(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Project).filter(Project.user_id == user.id).all()