from llama_index.core.schema import Document, BaseNode

from app.indexing.parsers.code_parser import CodeParser
from app.indexing.parsers.markdown_parser import MarkdownParser
from app.indexing.parsers.config_parser import ConfigParser


class RepositoryNodeParser:

    def __init__(self):

        self.code_parser = CodeParser()
        self.markdown_parser = MarkdownParser()
        self.config_parser = ConfigParser()

    def parse(self, documents: list[Document]) -> list[BaseNode]:

        nodes = []

        for document in documents:

            file_type = document.metadata["type"]

            if file_type == "SOURCE_CODE":
                nodes.extend(self.code_parser.parse(document))
                print(document.metadata["path"], "-> CODE")

            elif file_type == "DOCUMENTATION":
                nodes.extend(self.markdown_parser.parse(document))
                print(document.metadata["path"], "-> MARKDOWN")

            else:
                nodes.extend(self.config_parser.parse(document))
                print(document.metadata["path"], "-> CONFIG")

        return nodes