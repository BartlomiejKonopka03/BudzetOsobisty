from datetime import datetime
from functools import reduce

def zapisz_raport_do_pliku(budget, filename="raport.txt"):
    try:
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write("Miesięczne podsumowanie:\n")
            for month, total in budget.get_monthly_balance().items():
                file.write(f"{month}: {total:.2f} zł\n")

            file.write("\nPodsumowanie wg kategorii:\n")
            for cat, total in budget.get_category_summary().items():
                file.write(f"{cat}: {total:.2f} zł\n")

        print(f"Raport zapisany do pliku '{filename}'")
    except Exception as e:
        print(f"Błąd zapisu raportu: {e}")

def recursive_sum(transactions, index=0):
    if index >= len(transactions):
        return 0
    return transactions[index].amount + recursive_sum(transactions, index + 1)

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Wywołano funkcję: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def filter_transactions(transactions, condition_func):
    return [t for t in transactions if condition_func(t)]

def suma_reduce(transactions):
    return reduce(lambda acc, t: acc + t.amount, transactions, 0)