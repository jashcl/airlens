from fastapi import APIRouter
from ..schemas import ContentRequest
from ..services.content_generator import generate_content

router = APIRouter(prefix="/content", tags=["content"])

def _make(req: ContentRequest, kind: str): return generate_content(req.city, kind, req.audience, req.tone, req.topic)
@router.post("/blog-draft")
def blog(req: ContentRequest): return _make(req, "blog-draft")
@router.post("/linkedin-post")
def linkedin(req: ContentRequest): return _make(req, "linkedin-post")
@router.post("/awareness-points")
def awareness(req: ContentRequest): return _make(req, "awareness-points")
@router.post("/stakeholder-note")
def note(req: ContentRequest): return _make(req, "stakeholder-note")
