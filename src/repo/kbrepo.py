import json

from domain.kb_item import KBItem
from repo.base import PGRepo


class KBrepo(PGRepo):
    def __init__(self):
        super().__init__()

    def insert(self, kb_item: KBItem):
        values = f"""(
        :title,
        :description,
        :embedding)
        """
        params = kb_item.model_dump()

        self.execute(
            f"""
                     INSERT INTO knowledgebase (raw_title, raw_content, parsed_embedding) VALUES {values}
                     """,
            params,
        )

    def retrieve(self, embedded_query: list[float], count: int):
        values = self.select(
            """
        SELECT raw_content, parsed_embedding <-> :embedding_query as distance 
        FROM knowledgebase
        ORDER BY distance
        LIMIT :count
        """,
            {"embedding_query": json.dumps(embedded_query), "count": count},
        )
        return values
