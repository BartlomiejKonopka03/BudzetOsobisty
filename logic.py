from datetime import datetime

class Transaction:
    def __init__(self, amount, category, date, description=""):
        self.amount = float(amount)
        self.category = category
        self.date = self._parse_date(date)
        self.description = description

    def _parse_date(self, date_str):
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Nieprawidłowy format daty. Oczekiwany: RRRR-MM-DD")

    def __str__(self):
        return f"{self.date} | {self.category} | {self.amount:.2f} zł | {self.description}"

class IncomeTransaction(Transaction):
    def __init__(self, amount, date, description=""):
        super().__init__(amount, "Przychód", date, description)

class Budget:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        if not isinstance(transaction, Transaction):
            raise TypeError("Obiekt musi być typu Transaction")
        self.transactions.append(transaction)

    def get_monthly_balance(self):
        balance = {}
        for t in self.transactions:
            month = t.date.strftime("%Y-%m")
            balance[month] = balance.get(month, 0) + t.amount
        return balance

    def get_category_summary(self):
        summary = {}
        for t in self.transactions:
            summary[t.category] = summary.get(t.category, 0) + t.amount
        return summary
