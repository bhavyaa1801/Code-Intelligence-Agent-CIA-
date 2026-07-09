import os

from dotenv import load_dotenv
from llama_index.llms.google_genai import GoogleGenAI

load_dotenv()


class GeminiClient:

    def __init__(self):

        self.model = GoogleGenAI(
            model="gemini-2.5-flash",
            api_key=os.getenv("API_KEY"),
        )

    def generate_text(
        self,
        prompt: str,
    ) -> str:

        response = self.model.complete(prompt)

        return response.text

    def generate_structured(
        self,
        prompt: str,
    ) -> str:

        response = self.model.complete(prompt)

        return response.text