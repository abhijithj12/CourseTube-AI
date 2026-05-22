from pydantic import BaseModel
from typing import List, Optional

class TranscriptionOutput(BaseModel):
    text: str

class MetadataOutput(BaseModel):
    channel_name: str
    title: str
    content_type: str
    duration: Optional[int] = None
    video_count: Optional[int] = None
    video_urls: Optional[List[str]] = None

class StructuredOutput(BaseModel):
    module_no: int
    module_name: str
    module_description: str
    module_content: str
    
class CourseStructure(BaseModel):
    modules: List[StructuredOutput]

class NotesOutput(BaseModel):
    title: str
    notes: str
class QuizQuestion(BaseModel):
    question:str
    options: List[str]
    answer:str
class QuizOutput(BaseModel):
    questions: List[QuizQuestion]

class AssignmentOutput(BaseModel):
    title: str
    question: str
    

class ReviewOutput(BaseModel):
    module_title: str
    reviewed_notes: str
    reviewed_quiz: str
    reviewed_assignment: str
    quality_report: str

