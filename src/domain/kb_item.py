from pydantic import BaseModel, model_validator


class KBItem(BaseModel):
    title: str
    description: str
    content: str
    embedding: list[float] = [0.0] * 3072

    @model_validator(mode="after")
    def check_embedding_size(self):
        if len(self.embedding) != 3072:
            raise ValueError("wrong size")


class Query(BaseModel):
    query: str
