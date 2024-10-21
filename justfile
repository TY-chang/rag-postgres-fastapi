build:
    docker compose build

up:
    docker compose up -d

load_knowledge filename="":
    PYTHONPATH="$(pwd)/../src" python3 src/csv_loader.py -f {{filename}}