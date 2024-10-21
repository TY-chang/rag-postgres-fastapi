from adapter.openai import OpenAIClient
from domain.kb_item import Query
from repo.kbrepo import KBrepo


class AnswerKB:
    def __init__(self, kb_repo: KBrepo, openai_client: OpenAIClient):
        self.kb_repo = kb_repo
        self.openai_client = openai_client

    def get_openai_input(self, question: str, data: list[str]):
        system_prompt = f"""
        You are a professional customer support answering customer's question. The customer want to know about "{question}".
        Use the provided articles delimited by article tags to answer questions. If the answer cannot be found in the articles,
        write "I could not find an answer."
        provided articles : {';'.join(data)}
        """

        user_prompt = "summarize provided articles into relevant points to the question. Then suggest a proper, concise answer. Always write in the question's language. highlight the answer in bold."

        return system_prompt, user_prompt

    def execute(self, query: Query, count: int):
        # retrieve the embedding for the query
        embedding = self.openai_client.get_embedding(query.query)
        related_knowledge = self.kb_repo.retrieve(embedding, count)
        s, u = self.get_openai_input(
            query, [knowledge["raw_content"] for knowledge in related_knowledge]
        )
        answer = self.openai_client.get_answer(s, u)
        return answer
