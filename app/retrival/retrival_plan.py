from pydantic import BaseModel, Field


class RetrievalPlan(BaseModel):

    file_types: list[str] = Field(default_factory=list)

    languages: list[str] = Field(default_factory=list)

    top_k: int = 5

    confidence: float = 1.0

    

