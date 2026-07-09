from app.indexing.prompting.promt_builder import PromptBuilder
from app.retrival.repo_ret import RepositoryRetriever
from app.retrival.query_analyzer import QueryAnalyzer


class ChatService:

    def __init__(
        self,
        retriever: RepositoryRetriever,
        query_analyzer: QueryAnalyzer,
        prompt_builder: PromptBuilder,
        model,
    ):
        self.retriever = retriever
        self.query_analyzer = query_analyzer
        self.prompt_builder = prompt_builder
        self.model = model

    def ask(
        self,
        question: str
    ) -> str:

        request = self.query_analyzer.analyze(question)
        print(request)

        nodes = self.retriever.retrieve(request)

        for node in nodes:
          print(node.metadata)

    
        if not nodes:
          return "No relevant files were found for your query."
        
        # add a fallback if no result search all files 

        prompt = self.prompt_builder.build(
            question,
            nodes
        )

        answer = self.model.generate_text(prompt)

        return answer