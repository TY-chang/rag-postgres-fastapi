from sqlalchemy import Connection, create_engine, text

from settings import DB_DSN


class PGRepo:
    def __init__(self):
        self.engine = create_engine(DB_DSN)

    def execute(
        self, query: str, parameters: dict | None = None, conn: Connection | None = None
    ) -> list[dict] | None:
        rows = None
        if conn:
            cursor = conn.execute(text(query), parameters)
            if cursor.returns_rows:
                rows = cursor.mappings().fetchall()
        else:
            with self.engine.connect() as conn:
                cursor = conn.execute(text(query), parameters)
                if cursor.returns_rows:
                    rows = cursor.mappings().fetchall()
                conn.commit()
        return [dict(row) for row in rows] if rows is not None else rows

    def select(self, query: str, parameters: dict | None = None) -> list[dict]:
        rows = self.execute(query, parameters)
        assert rows is not None
        return rows
