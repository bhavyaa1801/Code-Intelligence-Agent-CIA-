from app.models.file_info import FileInfo

class RepositoryFilter:

    IGNORE_DIRS = {
        ".git",
        "node_modules",
        "__pycache__",
        "venv",
        ".venv",
        "dist",
        "build",
        ".idea",
        ".vscode",
        "coverage",
    }

    IGNORE_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico",

    ".mp4", ".mp3", ".wav",

    ".zip", ".tar", ".gz", ".7z", ".rar",

    ".exe", ".dll", ".so", ".dylib",

    ".pyc", ".class", ".o", ".obj",

    ".woff", ".woff2", ".ttf", ".otf",
}

    def filterr(self, files: list[FileInfo]) -> list[FileInfo]:

        filtered = []

        for file in files:

            if any(part in self.IGNORE_DIRS for part in file.relative_path.parts):
                file.ignored = True

            elif file.extension.lower() in self.IGNORE_EXTENSIONS:
                file.ignored = True

            filtered.append(file)

        return filtered