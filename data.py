import json
from logic import Transaction

def save_transactions_to_json(transactions, filename):
    data = [t.__dict__ for t in transactions]
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_transactions_from_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [Transaction(**item) for item in data]
    except FileNotFoundError:
        return []
