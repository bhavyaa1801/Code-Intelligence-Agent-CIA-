from pathlib import Path
from app.models.file_info import FileInfo


class RepositoryScanner:

    def scan(self, repo_path: Path) -> list[FileInfo]:

        files = []

        for file in repo_path.rglob("*"):

            if not file.is_file():
                continue

            info = FileInfo(
                relative_path=file.relative_to(repo_path),
                filename=file.name,
                extension=file.suffix,
                file_type="unknown",
                size=file.stat().st_size,
            )

            files.append(info)

        return files