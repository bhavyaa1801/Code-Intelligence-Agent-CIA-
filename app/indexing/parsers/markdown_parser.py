from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.schema import Document, BaseNode

from app.indexing.parsers.base_parser import BaseParser


class MarkdownParser(BaseParser):

    def __init__(self):
        self.splitter = SentenceSplitter(
            chunk_size=700,
            chunk_overlap=100,
        )

    def parse(self, document: Document) -> list[BaseNode]:
        return self.splitter.get_nodes_from_documents([document])