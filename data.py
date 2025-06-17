import csv
import os
from logic import Transaction

def save_transactions_to_csv(transactions, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    try:
        with open(filename, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["amount", "category", "date", "description"])
            for t in transactions:
                writer.writerow([t.amount, t.category, t.date.isoformat(), t.description])
    except Exception as e:
        print(f"Błąd zapisu: {e}")

def load_transactions_from_csv(filename):
    transactions = []
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    amount = float(row["amount"])
                    category = row["category"]
                    date = row["date"]
                    description = row.get("description", "")
                    transaction = Transaction(amount, category, date, description)
                    transactions.append(transaction)
                except Exception as e:
                    print(f"Błąd wczytywania wiersza: {e}")
    except FileNotFoundError:
        print("Plik nie istnieje – zaczynamy od pustej listy.")
    except Exception as e:
        print(f"Błąd odczytu pliku: {e}")
    return transactions
