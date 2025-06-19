from datetime import datetime

# Klasa reprezentująca jedną transakcję (przychód lub wydatek)
class Transaction:
    def __init__(self, amount, category, date, description=""):
        self.amount = float(amount)       # Kwota transakcji (może być dodatnia lub ujemna)
        self.category = category          # Kategoria transakcji (np. "Jedzenie", "Transport", "Przychód")
        self.date = self._parse_date(date)  # Data transakcji (parsowana jako obiekt typu date)
        self.description = description    # Opis transakcji (opcjonalny)

    def _parse_date(self, date_str):
        # Parsuje ciąg znaków do obiektu daty w formacie RRRR-MM-DD
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Nieprawidłowy format daty. Oczekiwany: RRRR-MM-DD")

    def __str__(self):
        # Zwraca reprezentację tekstową transakcji
        return f"{self.date} | {self.category} | {self.amount:.2f} zł | {self.description}"

# Klasa reprezentująca transakcję przychodu (zawsze pozytywna kwota i kategoria "Przychód")
class IncomeTransaction(Transaction):
    def __init__(self, amount, date, description=""):
        super().__init__(amount, "Przychód", date, description)

# Klasa przechowująca listę transakcji i udostępniająca metody analizy budżetu
class Budget:
    def __init__(self):
        self.transactions = []  # Lista przechowująca wszystkie transakcje

    def add_transaction(self, transaction):
        # Dodaje nową transakcję do listy
        if not isinstance(transaction, Transaction):
            raise TypeError("Obiekt musi być typu Transaction")
        self.transactions.append(transaction)

    def get_monthly_balance(self):
        # Zwraca słownik z saldem miesięcznym: {rok-miesiąc: suma kwot}
        balance = {}
        for t in self.transactions:
            month = t.date.strftime("%Y-%m")  # Ekstrakcja roku i miesiąca z daty
            balance[month] = balance.get(month, 0) + t.amount
        return balance

    def get_category_summary(self):
        # Zwraca sumy kwot według kategorii: {kategoria: suma kwot}
        summary = {}
        for t in self.transactions:
            summary[t.category] = summary.get(t.category, 0) + t.amount
        return summary
