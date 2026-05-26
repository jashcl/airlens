from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from ..schemas import ResearchBriefRequest
from ..services.report_generator import build_research_brief, build_latex_report

router = APIRouter(prefix="/reports", tags=["reports"])

@router.post("/research-brief")
def research_brief(req: ResearchBriefRequest):
    return build_research_brief(req.city, req.audience)

@router.get("/{city}/markdown", response_class=PlainTextResponse)
def markdown(city: str):
    return build_research_brief(city)["markdown_report"]

@router.get("/{city}/latex", response_class=PlainTextResponse)
def latex(city: str):
    return build_latex_report(city)
