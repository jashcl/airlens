from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

class DatasetUploadResponse(BaseModel):
    filename: str
    original_rows: int
    cleaned_rows: int
    duplicate_rows_removed: int
    columns: List[str]
    missing_values_before: Dict[str, int]
    missing_values_after: Dict[str, int]
    detected_cities: List[str]
    detected_pollutants: List[str]
    min_date: str
    max_date: str
    preview_rows: List[Dict[str, Any]]

class ResearchBriefRequest(BaseModel):
    city: str
    audience: str = "technical"

class ContentRequest(BaseModel):
    city: str
    audience: str = "public"
    tone: str = "formal"
    topic: Optional[str] = None

class StakeholderBase(BaseModel):
    name: str
    organization: str
    organization_type: str = "NGO"
    city: Optional[str] = None
    email: Optional[str] = None
    phone_or_linkedin: Optional[str] = None
    interest_area: Optional[str] = None
    status: str = "Not Contacted"
    notes: Optional[str] = None
    last_contacted: Optional[str] = None
    next_followup: Optional[str] = None
    draft_message: Optional[str] = None

class StakeholderCreate(StakeholderBase):
    pass

class StakeholderUpdate(BaseModel):
    name: Optional[str] = None
    organization: Optional[str] = None
    organization_type: Optional[str] = None
    city: Optional[str] = None
    email: Optional[str] = None
    phone_or_linkedin: Optional[str] = None
    interest_area: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    last_contacted: Optional[str] = None
    next_followup: Optional[str] = None
    draft_message: Optional[str] = None

class StakeholderOut(StakeholderBase):
    id: int
    created_at: Any
    updated_at: Any
    class Config:
        from_attributes = True

class GenerateEmailRequest(BaseModel):
    city: str

class ResearchLogBase(BaseModel):
    title: str
    topic: Optional[str] = None
    source_name: Optional[str] = None
    source_url: Optional[str] = None
    summary: Optional[str] = None
    tags: Optional[str] = None
    status: str = "Draft"

class ResearchLogCreate(ResearchLogBase):
    pass

class ResearchLogUpdate(BaseModel):
    title: Optional[str] = None
    topic: Optional[str] = None
    source_name: Optional[str] = None
    source_url: Optional[str] = None
    summary: Optional[str] = None
    tags: Optional[str] = None
    status: Optional[str] = None

class ResearchLogOut(ResearchLogBase):
    id: int
    created_at: Any
    updated_at: Any
    class Config:
        from_attributes = True

class BioCompareRequest(BaseModel):
    city: str
    pollutant: str
    before_value: float = Field(gt=0)
    after_value: float = Field(ge=0)
    intervention_type: str = "Biofiltration observation"
