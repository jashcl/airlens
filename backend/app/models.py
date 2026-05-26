from datetime import datetime
from sqlalchemy import Column, DateTime, Float, Integer, String, Text
from .database import Base

class Stakeholder(Base):
    __tablename__ = "stakeholders"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(160), nullable=False)
    organization = Column(String(200), nullable=False)
    organization_type = Column(String(80), nullable=False, default="NGO")
    city = Column(String(120), nullable=True)
    email = Column(String(200), nullable=True)
    phone_or_linkedin = Column(String(250), nullable=True)
    interest_area = Column(String(250), nullable=True)
    status = Column(String(80), nullable=False, default="Not Contacted")
    notes = Column(Text, nullable=True)
    last_contacted = Column(String(40), nullable=True)
    next_followup = Column(String(40), nullable=True)
    draft_message = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class ResearchLog(Base):
    __tablename__ = "research_logs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(220), nullable=False)
    topic = Column(String(120), nullable=True)
    source_name = Column(String(220), nullable=True)
    source_url = Column(String(500), nullable=True)
    summary = Column(Text, nullable=True)
    tags = Column(String(300), nullable=True)
    status = Column(String(60), nullable=False, default="Draft")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class InterventionRecord(Base):
    __tablename__ = "intervention_records"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(120), nullable=False)
    pollutant = Column(String(40), nullable=False)
    before_value = Column(Float, nullable=False)
    after_value = Column(Float, nullable=False)
    reduction_percent = Column(Float, nullable=False)
    intervention_type = Column(String(180), nullable=False)
    observation_note = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
