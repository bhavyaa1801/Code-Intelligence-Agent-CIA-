from app.models.file_info import FileInfo


class RepositoryClassifier:

    SOURCE_CODE = {
        ".js",".jsx",".ts",".tsx",".mjs",".cjs",".py", ".pyi",".go",".java" , ".kt" , ".kts", ".cs" , ".c",".cpp",".cc",".cxx",".h",".hpp", ".rs", ".php",".rb",".swift",".dart",".sh",".bash",".zsh",".ps1",".html",".css",".scss",".sass",".less",".sql", ".proto", ".html"

    }

    DOCUMENTATION = {
    "readme.md",
    "changelog.md",
    "contributing.md",
    "license",
    "license.md",
    "code_of_conduct.md",
    "security.md",
    } 
   
    DEPENDENCY_FILES = {
        "requirements.txt",
        "package.json",
        "package-lock.json",
        "settings.json",
        "tsconfig.json",
        "go.mod",
        "go.sum",
        "pom.xml",
        "Cargo.toml",
        "Cargo.lock",
        "pyproject.toml",
        "pnpm-lock.yaml",
        "yarn.lock",
        "bun.lockb",
        "poetry.lock",
        "Pipfile",
        "Pipfile.lock",
        "composer.json",
        "composer.lock",
    }

    CONFIG_FILES = {
        ".env",
        ".env.local",
        ".env.development",
        ".env.production",
        "config.yaml",
        "config.yml",
        "eslint.config.js",
        ".prettierrc",
        ".editorconfig",
        ".gitignore",
        ".gitattributes",
        ".vscode/settings.json"

    }

    INFRASTRUCTURE_FILES = {
        "dockerfile",
        "docker-compose.yml",
        "docker-compose.yaml",
        "Jenkinsfile",
        "Makefile",
        "Taskfile.yml"

    }

    BINARY = {
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".bmp",
    ".ico",
    ".svg",
    ".zip",
    ".tar",
    ".gz",
    ".7z",
    ".rar",
    ".exe",
    ".dll",
    ".so",
    ".dylib",
    ".class",
    ".jar",
    ".pyc",
    ".o",
    ".obj",
    ".ttf",
    ".otf",
    ".woff",
    ".woff2",
    }



    def classify(self, files: list[FileInfo]) -> list[FileInfo]:
        
        for file in files:

            name = file.filename.lower()
            ext = file.extension.lower()
            path = str(file.relative_path).lower()

            if file.ignored:
                continue

            elif ".github/workflows" in path:
                file.file_type = "CI_CD"

            elif name in self.INFRASTRUCTURE_FILES:
                file.file_type = "INFRASTRUCTURE"

            elif name in self.DEPENDENCY_FILES:
                file.file_type = "DEPENDENCIES"

            elif name in self.CONFIG_FILES:
                file.file_type = "CONFIG"

            elif ext in self.BINARY:
                file.file_type = "BINARY"

            elif name in self.DOCUMENTATION or path.startswith("docs"):
                file.file_type = "DOCUMENTATION"

            elif ext in self.SOURCE_CODE:
                file.file_type = "SOURCE_CODE"

                if ext == ".go":
                    file.language = "go"

                elif ext in {".js", ".jsx"}:
                    file.language = "javascript"

                elif ext in {".ts", ".tsx"}:
                    file.language = "typescript"

                elif ext == ".py":
                    file.language = "python"

                else:
                    file.file_type = "OTHER"

        return files