from app.llm.gemini import GeminiClient
from app.retrival.planner import PLANNER_PROMPT
from app.retrival.retrival_plan import RetrievalPlan
from app.retrival.retrival_req import RetrievalRequest


class QueryAnalyzer:

    def __init__(self):

        self.model = GeminiClient()

    def analyze(
        self,
        question: str,
    ) -> RetrievalRequest:

        prompt = f"""
{PLANNER_PROMPT}

Question:

{question}

Output:
"""

        response = (
        self.model.generate_structured(prompt)
        .replace("```json", "")
        .replace("```", "")
        .strip()
         )
        
        print("\nPlanner Response:\n")
        print(response)

        plan = RetrievalPlan.model_validate_json(response)
        print(plan)

        return RetrievalRequest(
            question=question,
            file_types=plan.file_types,
            languages=plan.languages,
            top_k=plan.top_k,
        )