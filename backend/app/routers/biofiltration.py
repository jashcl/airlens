from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import InterventionRecord
from ..schemas import BioCompareRequest
from ..services.biofiltration_service import compare_intervention

router = APIRouter(prefix="/biofiltration", tags=["biofiltration"])

@router.post("/compare")
def compare(req: BioCompareRequest, db: Session = Depends(get_db)):
    result = compare_intervention(req.city, req.pollutant, req.before_value, req.after_value, req.intervention_type)
    obj = InterventionRecord(city=req.city, pollutant=req.pollutant, before_value=req.before_value, after_value=req.after_value, reduction_percent=result["reduction_percent"], intervention_type=req.intervention_type, observation_note=result["observation_note"])
    db.add(obj); db.commit(); db.refresh(obj)
    return {**result, "id": obj.id}

@router.get("/records")
def records(db: Session = Depends(get_db)):
    rows = db.query(InterventionRecord).order_by(InterventionRecord.created_at.desc()).limit(50).all()
    return [{"id": r.id, "city": r.city, "pollutant": r.pollutant, "before_value": r.before_value, "after_value": r.after_value, "reduction_percent": r.reduction_percent, "intervention_type": r.intervention_type, "observation_note": r.observation_note, "created_at": r.created_at} for r in rows]
