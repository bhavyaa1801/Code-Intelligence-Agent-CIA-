from llama_index.core import VectorStoreIndex

from app.indexing.node_parser import RepositoryNodeParser


class IndexBuilder:

    def build(self, documents):

        parser = RepositoryNodeParser()

        nodes = parser.parse(documents)

        return VectorStoreIndex(nodes)