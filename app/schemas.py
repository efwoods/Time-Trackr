from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class CategoryCreate(BaseModel):
    name: str

class CategoryOut(BaseModel):
    id: int
    name: str
    user_id: int

    class Config:
        orm_mode = True

class ProjectCreate(BaseModel):
    name: str
    category_id: int

class ProjectOut(BaseModel):
    id: int
    name: str
    user_id: int
    category_id: int

    class Config:
        orm_mode = True

class TimeEntryCreate(BaseModel):
    project_id: int
    hours: float
    description: Optional[str] = None

class TimeEntryOut(BaseModel):
    id: int
    project_id: int
    hours: float
    description: Optional[str]
    timestamp: datetime

    class Config:
        orm_mode = True

class LLMSummaryCreate(BaseModel):
    summary: str

class LLMSummaryOut(BaseModel):
    id: int
    summary: str
    timestamp: datetime

    class Config:
        orm_mode = True

class CategorySummary(BaseModel):
    category_id: int
    category_name: str
    total_hours: float