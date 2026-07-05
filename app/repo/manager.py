from pathlib import Path
from git import Repo

class RepositoryManager:

    def __init__(self):
        self.base_path = Path("data/repositories")
        self.base_path.mkdir(parents=True, exist_ok=True)

    def get_repo_name(self, repo_url: str) -> str:
     return repo_url.rstrip("/").split("/")[-1].replace(".git", "")

    def clone(self, repo_url: str) -> Path:

     repo_name = self.get_repo_name(repo_url)

     repo_path = self.base_path / repo_name

     if repo_path.exists():
        print("Repository already exists.")
        return repo_path

     Repo.clone_from(repo_url, repo_path)

     return repo_path

    def update(self):
        pass

    def delete(self):
        pass




