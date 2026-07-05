from llama_index.core.schema import NodeWithScore


class PromptBuilder:
    """
    Builds the final prompt that will be sent to the LLM.

    Responsibility:
        Retrieved Nodes + User Question -> Prompt String
    """

    SEPARATOR = "=" * 80
    DIVIDER = "-" * 80

    def build(
        self,
        question: str,
        nodes: list[NodeWithScore]
    ) -> str:

        parts: list[str] = []

        # ------------------------------------------------------------------
        # System Instructions
        # ------------------------------------------------------------------

        parts.append(
            "You are an expert software engineer.\n"
            "Answer the user's question ONLY using the provided repository context.\n"
            "If the answer cannot be found in the context, say you don't know.\n\n"
        )

        # ------------------------------------------------------------------
        # Repository Context
        # ------------------------------------------------------------------

        parts.append(f"{self.SEPARATOR}\n")
        parts.append("Repository Context\n")
        parts.append(f"{self.SEPARATOR}\n\n")

        for node in nodes:

            metadata = node.node.metadata
            text = node.node.text

            parts.append(f"File: {metadata.get('filename', 'Unknown')}\n")
            parts.append(f"Path: {metadata.get('path', 'Unknown')}\n")
            parts.append(f"Type: {metadata.get('type', 'Unknown')}\n")
            parts.append(f"Language: {metadata.get('language', 'Unknown')}\n\n")

            parts.append("Content:\n")
            parts.append(text)
            parts.append("\n\n")
            parts.append(f"{self.DIVIDER}\n\n")

        # ------------------------------------------------------------------
        # User Question
        # ------------------------------------------------------------------

        parts.append(f"{self.SEPARATOR}\n")
        parts.append("User Question\n")
        parts.append(f"{self.SEPARATOR}\n\n")

        parts.append(question)

        return "".join(parts)