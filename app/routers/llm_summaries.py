from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import LLMSummary
from app.schemas import LLMSummaryCreate, LLMSummaryOut
from app.dependencies import get_db, get_current_user
import httpx

router = APIRouter()

async def fetch_llm_summary():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                settings.LLM_API_URL,
                headers={"Authorization": f"Bearer {settings.LLM_API_KEY}"}
            )
            response.raise_for_status()
            return response.json().get("summary", "No summary provided")
        except httpx.HTTPError:
            raise HTTPException(status_code=503, detail="Failed to fetch LLM summary")

@router.post("/", response_model=LLMSummaryOut)
async def create_llm_summary(db: Session = Depends(get_db), user=Depends(get_current_user)):
    summary_text = await fetch_llm_summary()
    db_summary = LLMSummary(summary=summary_text, user_id=user.id)
    db.add(db_summary)
    db.commit()
    db.refresh(db_summary)
    return db_summary

@router.get("/", response_model=list[LLMSummaryOut])
def read_llm_summaries(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(LLMSummary).filter(LLMSummary.user_id == user.id).all()