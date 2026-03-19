import json
import random
from pathlib import Path

DIR = Path(__file__).parent
ASCII_DB_PATH = DIR / "ascii_database.json"
MAX_WIDTH = 24

with open(ASCII_DB_PATH, "r") as f:
    ASCII_DB = json.load(f)

def get_ascii_art(module_count):
    matching = [
        item for item in ASCII_DB
        if item.get("height") == module_count
        and item.get("width", 0) <= MAX_WIDTH
    ]

    if not matching:
        raise ValueError(f"No ASCII art matches height={module_count}, width<={MAX_WIDTH}")

    return random.choice(matching)["art"].split("\n")
