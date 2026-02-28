import json
import random
from pathlib import Path

DIR = Path(__file__).parent
ASCII_DB_PATH = DIR / "ascii_database.json"
MAX_WIDTH = 24 # max height & width 

def get_ascii_art(module_count):
    with open(ASCII_DB_PATH, "r") as f:
        ascii_db = json.load(f)
    # filters by height and width
    matching_art = [
        item for item in ascii_db
        if item.get("height") == module_count and item.get("width") <= MAX_WIDTH
    ]

    if not matching_art:
        raise ValueError("No ASCII art matches the constraints.")

    selected_art = random.choice(matching_art)["art"].split("\n") #random selection

    return selected_art