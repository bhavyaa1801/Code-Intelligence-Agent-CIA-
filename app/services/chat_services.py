from app.indexing.prompting.promt_builder import PromptBuilder
from app.retrival.repo_ret import RepositoryRetriever


class ChatService:

    def __init__(
        self,
        retriever: RepositoryRetriever,
        prompt_builder: PromptBuilder,
        model,
    ):
        self.retriever = retriever
        self.prompt_builder = prompt_builder
        self.model = model

    def ask(
        self,
        question: str
    ) -> str:

        nodes = self.retriever.retrieve(question)

        prompt = self.prompt_builder.build(
            question,
            nodes
        )

        response = self.model.generate(prompt)

        return response