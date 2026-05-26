from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Stakeholder
from ..schemas import StakeholderCreate, StakeholderUpdate, StakeholderOut, GenerateEmailRequest
from ..services.outreach_generator import generate_email

router = APIRouter(prefix="/outreach", tags=["outreach"])

@router.post("/stakeholders", response_model=StakeholderOut)
def create_stakeholder(payload: StakeholderCreate, db: Session = Depends(get_db)):
    obj = Stakeholder(**payload.model_dump())
    db.add(obj); db.commit(); db.refresh(obj); return obj

@router.get("/stakeholders", response_model=list[StakeholderOut])
def list_stakeholders(db: Session = Depends(get_db)):
    return db.query(Stakeholder).order_by(Stakeholder.created_at.desc()).all()

@router.get("/stakeholders/{stakeholder_id}", response_model=StakeholderOut)
def get_stakeholder(stakeholder_id: int, db: Session = Depends(get_db)):
    obj = db.get(Stakeholder, stakeholder_id)
    if not obj: raise HTTPException(404, "Stakeholder not found")
    return obj

@router.put("/stakeholders/{stakeholder_id}", response_model=StakeholderOut)
def update_stakeholder(stakeholder_id: int, payload: StakeholderUpdate, db: Session = Depends(get_db)):
    obj = db.get(Stakeholder, stakeholder_id)
    if not obj: raise HTTPException(404, "Stakeholder not found")
    for k, v in payload.model_dump(exclude_unset=True).items(): setattr(obj, k, v)
    db.commit(); db.refresh(obj); return obj

@router.delete("/stakeholders/{stakeholder_id}")
def delete_stakeholder(stakeholder_id: int, db: Session = Depends(get_db)):
    obj = db.get(Stakeholder, stakeholder_id)
    if not obj: raise HTTPException(404, "Stakeholder not found")
    db.delete(obj); db.commit(); return {"deleted": True}

@router.post("/stakeholders/{stakeholder_id}/generate-email")
def gen_email(stakeholder_id: int, payload: GenerateEmailRequest, db: Session = Depends(get_db)):
    obj = db.get(Stakeholder, stakeholder_id)
    if not obj: raise HTTPException(404, "Stakeholder not found")
    email = generate_email(obj, payload.city)
    obj.draft_message = email["email_body"]
    db.commit()
    return email
