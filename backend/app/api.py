from fastapi import FastAPI
import json
import os


app = FastAPI()


mock_items = [
    {"id": 1, "name": "Grilled Chicken", "outlet": "cafe1"},
    {"id": 2, "name": "Beef Stew", "outlet": "cafe1"},
    {"id": 3, "name": "Cocktail Shrimp", "outlet": "bar2"}
]

def load_items():
    file_path = os.path.join(os.path.dirname(__file__), '/Users/mikemyers/Library/CloudStorage/ProtonDrive-mimyers@proton.me-folder/Label App/backend/data/items.json')
    with open(file_path, 'r') as f:
        return json.load(f)

@app.get('/items')
def get_items(outlet: str):
    items = load_items()
    filtered_items = [item for item in mock_items if item['outlet'] == outlet]
    return filtered_items

@app.post('/print-label')
def print_label(item: dict):
    return {'status': 'print queued', 'item': item}

