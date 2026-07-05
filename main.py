from app.repo.manager import RepositoryManager
from app.repo.scanner import RepositoryScanner
from app.repo.filter import RepositoryFilter
from app.repo.classifier import RepositoryClassifier

from app.indexing.document_builder import DocumentBuilder
from app.indexing.node_parser import RepositoryNodeParser
from app.indexing.index_builder import IndexBuilder

from app.retrival.repo_ret import RepositoryRetriever
from app.indexing.prompting.promt_builder import PromptBuilder
from app.services.chat_services import ChatService

from app.llm import settings
from app.llm.gemini import GeminiClient


def main():

    manager = RepositoryManager()
    scanner = RepositoryScanner()
    classifier = RepositoryClassifier()
    filterr = RepositoryFilter()

    repo = manager.clone(
        "https://github.com/bhavyaa1801/SUBMITIFY"
    )

    files = scanner.scan(repo)
    files = filterr.filterr(files)
    files = classifier.classify(files)

    document_builder = DocumentBuilder()
    documents = document_builder.build(repo, files)

    parser = RepositoryNodeParser()
    nodes = parser.parse(documents)

    print(f"Documents : {len(documents)}")
    print(f"Nodes     : {len(nodes)}")


    index_builder = IndexBuilder()
    index = index_builder.build(documents)

    retriever = RepositoryRetriever(index)

    prompt_builder = PromptBuilder()

    chat = ChatService(
        retriever=retriever,
        prompt_builder=prompt_builder,
        model=GeminiClient(),
    )

    while True:

        question = input("\nYou > ")

        if question.lower() in {"exit", "quit"}:
            break

        answer = chat.ask(question)

        print("\nCIA >", answer)


if __name__ == "__main__":
    main()