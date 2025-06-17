from logic import Transaction

class Budget:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        if not isinstance(transaction, Transaction):
            raise TypeError("Obiekt musi być typu Transaction")
        self.transactions.append(transaction)

    def edit_transaction(self, index, new_transaction):
        if index < 0 or index >= len(self.transactions):
            raise IndexError("Nieprawidłowy indeks transakcji.")
        if not isinstance(new_transaction, Transaction):
            raise TypeError("Obiekt musi być typu Transaction")
        self.transactions[index] = new_transaction

    def delete_transaction(self, index):
        if index < 0 or index >= len(self.transactions):
            raise IndexError("Nieprawidłowy indeks transakcji.")
        del self.transactions[index]

    def get_monthly_summary(self):
        summary = {}
        for t in self.transactions:
            month = t.date.strftime("%Y-%m")
            summary[month] = summary.get(month, 0) + t.amount
        return summary

    def get_category_summary(self):
        summary = {}
        for t in self.transactions:
            summary[t.category] = summary.get(t.category, 0) + t.amount
        return summary

    def get_total_income(self):
        return sum(t.amount for t in self.transactions if t.amount > 0)

    def get_total_expense(self):
        return sum(t.amount for t in self.transactions if t.amount < 0)

    def get_monthly_balance(self):
        balance = {}
        for t in self.transactions:
            month = t.date.strftime("%Y-%m")
            balance[month] = balance.get(month, 0) + t.amount
        return balance

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
