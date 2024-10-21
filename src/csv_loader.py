import argparse
import csv
import os
from typing import List

import openai
from sqlalchemy import create_engine

from domain.kb_item import KBItem
from repo.kbrepo import KBrepo
from settings import DB_DSN, OPENAI_API_KEY

# Set up OpenAI API key
openai.api_key = OPENAI_API_KEY

# Setup connection to the database
engine = create_engine(DB_DSN)
kb_repo = KBrepo()


def get_embedding(text: str, model: str = "text-embedding-3-large") -> List[float]:
    """
    Get the embedding for a given text using OpenAI's API.

    :param text: The text to embed
    :return: A list of floats representing the embedding
    """
    text = text.replace("\n", " ")
    response = openai.embeddings.create(input=[text], model=model).data[0].embedding
    return response


def load_csv_to_database(csv_path: str):
    """
    Load data from a CSV file into the database.

    :param csv_path: Path to the CSV file
    :param db_session: SQLAlchemy database session
    """
    with open(csv_path, "r", encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            title = row.get("title", "")
            description = row.get("description", "")

            # Combine title and description for embedding
            content = (
                f"<title>{title}</title>\n<description>{description}</description>"
            )

            # Generate embedding for the content
            embedding = get_embedding(content)

            kb_item = KBItem(
                title=title,
                description=description,
                content=content,
                embedding=embedding,
            )
            # insert into database
            kb_repo.insert(kb_item)


def main(filename: str):
    # Path to the CSV file
    csv_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "data", filename)
    )

    try:
        # Load CSV data into the database
        load_csv_to_database(csv_path)
        print("CSV data successfully loaded into the database.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Load CSV data into the database")
    parser.add_argument(
        "-f", "--filename", type=str, help="Path to the CSV file", default="cs.csv"
    )
    args = parser.parse_args()
    main(args.filename)
