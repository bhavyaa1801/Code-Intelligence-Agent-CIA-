from pathlib import Path
from llama_index.core import Document
from app.models.file_info import FileInfo

class DocumentBuilder:

    def build(
        self,
        repo_path: Path,
        files: list[FileInfo]
    ) -> list[Document]:

       documents = []

       for file in files:

        if file.ignored:
         continue

        if file.file_type == "BINARY" :
          continue

        absolute_path = repo_path / file.relative_path

        text = absolute_path.read_text(
        encoding="utf-8",
        errors="ignore"
         )

        doc = Document(
        text=text,
        metadata={
            "path": str(file.relative_path),
            "filename": file.filename,
            "extension": file.extension,
            "type": file.file_type,
            "language": file.language
        },
        )

        documents.append(doc)
       return documents
 
        