import json
from logic import Transaction

# Funkcja zapisuje listę obiektów Transaction do pliku JSON.
# Parametry:
# - transactions: lista obiektów Transaction
# - filename: ścieżka do pliku, do którego zapisane zostaną dane
def save_transactions_to_json(transactions, filename):
    data = [t.__dict__ for t in transactions]  # konwersja obiektów do słowników
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)  # zapis do pliku JSON

# Funkcja wczytuje dane transakcji z pliku JSON i zwraca listę obiektów Transaction.
# Parametr:
# - filename: ścieżka do pliku z zapisanymi danymi
# Zwraca:
# - lista obiektów Transaction lub pustą listę, jeśli plik nie istnieje
def load_transactions_from_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)  # wczytanie danych JSON jako listy słowników
        return [Transaction(**item) for item in data]  # odtworzenie obiektów Transaction
    except FileNotFoundError:
        return []  # jeśli plik nie istnieje, zwracamy pustą listę
