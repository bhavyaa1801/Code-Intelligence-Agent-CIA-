from llama_index.core import VectorStoreIndex
from llama_index.core.schema import NodeWithScore


class RepositoryRetriever:

    def __init__(
        self,
        index: VectorStoreIndex,
        similarity_top_k: int = 5
    ):
        self.retriever = index.as_retriever(
            similarity_top_k=similarity_top_k
        )

    def retrieve(
        self,
        question: str
    ) -> list[NodeWithScore]:
        return self.retriever.retrieve(question)