from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.schema import Document, BaseNode

from app.indexing.parsers.base_parser import BaseParser


class CodeParser(BaseParser):

    def __init__(self):
        self.splitter = SentenceSplitter(
            chunk_size=512,
            chunk_overlap=50,
        )

    def parse(self, document: Document) -> list[BaseNode]:
        return self.splitter.get_nodes_from_documents([document])