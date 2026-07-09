from dataclasses import dataclass, field


@dataclass
class RetrievalRequest:

    question: str

    top_k: int = 5

    file_types: list[str] = field(default_factory=list)

    languages: list[str] = field(default_factory=list)

    # Future features
    use_hybrid_search: bool = False
    use_reranker: bool = False