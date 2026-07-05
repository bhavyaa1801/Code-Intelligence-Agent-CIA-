from abc import ABC, abstractmethod

from llama_index.core.schema import Document, BaseNode


class BaseParser(ABC):

    @abstractmethod
    def parse(self, document: Document) -> list[BaseNode]:
        pass