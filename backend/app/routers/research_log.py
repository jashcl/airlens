from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_
from ..database import get_db
from ..models import ResearchLog
from ..schemas import ResearchLogCreate, ResearchLogUpdate, ResearchLogOut

router = APIRouter(prefix="/research-log", tags=["research-log"])

@router.post("", response_model=ResearchLogOut)
def create_log(payload: ResearchLogCreate, db: Session = Depends(get_db)):
    obj = ResearchLog(**payload.model_dump()); db.add(obj); db.commit(); db.refresh(obj); return obj

@router.get("", response_model=list[ResearchLogOut])
def list_logs(topic: str | None = None, status: str | None = None, tag: str | None = None, search: str | None = None, db: Session = Depends(get_db)):
    q = db.query(ResearchLog)
    if topic: q = q.filter(ResearchLog.topic.ilike(f"%{topic}%"))
    if status: q = q.filter(ResearchLog.status == status)
    if tag: q = q.filter(ResearchLog.tags.ilike(f"%{tag}%"))
    if search: q = q.filter(or_(ResearchLog.title.ilike(f"%{search}%"), ResearchLog.summary.ilike(f"%{search}%")))
    return q.order_by(ResearchLog.created_at.desc()).all()

@router.put("/{log_id}", response_model=ResearchLogOut)
def update_log(log_id: int, payload: ResearchLogUpdate, db: Session = Depends(get_db)):
    obj = db.get(ResearchLog, log_id)
    if not obj: raise HTTPException(404, "Research log not found")
    for k, v in payload.model_dump(exclude_unset=True).items(): setattr(obj, k, v)
    db.commit(); db.refresh(obj); return obj

@router.delete("/{log_id}")
def delete_log(log_id: int, db: Session = Depends(get_db)):
    obj = db.get(ResearchLog, log_id)
    if not obj: raise HTTPException(404, "Research log not found")
    db.delete(obj); db.commit(); return {"deleted": True}
