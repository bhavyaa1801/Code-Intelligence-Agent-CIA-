from llama_index.core import VectorStoreIndex
from llama_index.core.schema import NodeWithScore
from llama_index.core.vector_stores import MetadataFilter, MetadataFilters

from app.retrival.retrival_req import RetrievalRequest


class RepositoryRetriever:

    def __init__(
        self,
        index: VectorStoreIndex,
    ):
        self.index = index

    def retrieve(
        self,
        request: RetrievalRequest,
    ) -> list[NodeWithScore]:

        filters = None

        if request.file_types:

            filters = MetadataFilters(
                filters=[
                    MetadataFilter(
                        key="type",
                        value=file_type,
                    )
                    for file_type in request.file_types
                ]
            )

        retriever = self.index.as_retriever(
            similarity_top_k=request.top_k,
            filters=filters,
        )

        return retriever.retrieve(
            request.question
        )