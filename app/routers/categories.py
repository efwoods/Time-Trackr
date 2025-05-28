from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Category
from app.schemas import CategoryCreate, CategoryOut
from app.dependencies import get_db, get_current_user

router = APIRouter()

@router.post("/", response_model=CategoryOut)
def create_category(category: CategoryCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_category = Category(**category.dict(), user_id=user.id)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.get("/", response_model=list[CategoryOut])
def read_categories(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Category).filter(Category.user_id == user.id).all()