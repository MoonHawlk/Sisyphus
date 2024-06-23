from dotenv import load_dotenv

load_dotenv()

from llama_index.core.agent import ReActAgent
from llama_index.llms.ollama import Ollama
from llama_index.core.tools import FunctionTool


class RAG:
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers and returns the product"""
        return a * b

    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers and returns the sum"""
        return a + b

    def __init__(self):
        self.add_tool = FunctionTool.from_defaults(fn=self.add)
        self.multiply_tool = FunctionTool.from_defaults(fn=self.multiply)

        self.llm = Ollama(model="Valoryun")
        self.agent = ReActAgent.from_tools([self.multiply_tool, self.add_tool], llm=self.llm, verbose=True)

    def chat_rag(self, input_text):
        try:
            response = self.agent.chat(input_text)
            return str(response)

        except Exception as e:
            erro = "NÃO FOI POSSIVEL ACHAR SUA RESPOSTA"
            return erro
