from fastapi import FastAPI

app = FastAPI()


mock_items = [
    {"id": 1, "name": "Grilled Chicken", "outlet": "cafe1"},
    {"id": 2, "name": "Beef Stew", "outlet": "cafe1"},
    {"id": 3, "name": "Cocktail Shrimp", "outlet": "bar2"}
]

@app.get('/items')
def get_items(outlet: str):
    filtered_items = [item for item in mock_items if item['outlet'] == outlet]
    return filtered_items

@app.post('/print-label')
def print_label(item: dict):
    return {'status': 'print queued', 'item': item}

