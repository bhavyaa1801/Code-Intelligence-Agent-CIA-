from pathlib import Path

import chromadb

from llama_index.core import VectorStoreIndex
from llama_index.core.storage.storage_context import StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore


class IndexBuilder:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="data/chroma"
        )

    def build(
        self,
        repo_name: str,
        nodes,
    ) -> VectorStoreIndex:


        collection = self.client.get_or_create_collection(
            name=repo_name
        )

        vector_store = ChromaVectorStore(
            chroma_collection=collection
        )

        storage_context = StorageContext.from_defaults(
            vector_store=vector_store
        )

        if collection.count() == 0:

            print(f"Building index for '{repo_name}'...")

            index = VectorStoreIndex(
                nodes,
                storage_context=storage_context,
            )

        else:

            print(f"Loading existing index for '{repo_name}'...")

            index = VectorStoreIndex.from_vector_store(
                vector_store=vector_store,
            )

        return index