from logic import Transaction

class Budget:
    # Konstruktor inicjalizuje pustą listę transakcji
    def __init__(self):
        self.transactions = []

    # Dodaje nową transakcję do budżetu
    def add_transaction(self, transaction):
        if not isinstance(transaction, Transaction):
            raise TypeError("Obiekt musi być typu Transaction")
        self.transactions.append(transaction)

    # Edytuje istniejącą transakcję na wskazanym indeksie
    def edit_transaction(self, index, new_transaction):
        if index < 0 or index >= len(self.transactions):
            raise IndexError("Nieprawidłowy indeks transakcji.")
        if not isinstance(new_transaction, Transaction):
            raise TypeError("Obiekt musi być typu Transaction")
        self.transactions[index] = new_transaction

    # Usuwa transakcję ze wskazanego indeksu
    def delete_transaction(self, index):
        if index < 0 or index >= len(self.transactions):
            raise IndexError("Nieprawidłowy indeks transakcji.")
        del self.transactions[index]

    # Zwraca słownik sum kwot transakcji pogrupowanych według miesiąca
    def get_monthly_summary(self):
        summary = {}
        for t in self.transactions:
            month = t.date.strftime("%Y-%m")
            summary[month] = summary.get(month, 0) + t.amount
        return summary

    # Zwraca słownik sum kwot transakcji pogrupowanych według kategorii
    def get_category_summary(self):
        summary = {}
        for t in self.transactions:
            summary[t.category] = summary.get(t.category, 0) + t.amount
        return summary

    # Oblicza sumę wszystkich przychodów (transakcji dodatnich)
    def get_total_income(self):
        return sum(t.amount for t in self.transactions if t.amount > 0)

    # Oblicza sumę wszystkich wydatków (transakcji ujemnych)
    def get_total_expense(self):
        return sum(t.amount for t in self.transactions if t.amount < 0)

    # Zwraca bilans (saldo) miesięczny na podstawie wszystkich transakcji
    def get_monthly_balance(self):
        balance = {}
        for t in self.transactions:
            month = t.date.strftime("%Y-%m")
            balance[month] = balance.get(month, 0) + t.amount
        return balance

    # Zwraca osobno sumy przychodów i wydatków dla każdego miesiąca
    def get_monthly_income_expense(self):
        summary = {}
        for t in self.transactions:
            month = t.date.strftime("%Y-%m")
            if month not in summary:
                summary[month] = [0, 0]
            if t.amount > 0:
                summary[month][0] += t.amount
            else:
                summary[month][1] += t.amount
        return summary
