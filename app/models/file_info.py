from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

class FileInfo(BaseModel):
    relative_path: Path
    filename: str
    extension: str

    file_type: str = "OTHER"
    language: str = "unknown"

    size: int
    ignored: bool = False

    metadata: dict[str, Any] = Field(default_factory=dict)