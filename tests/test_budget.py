import unittest
from budget import Budget
from logic import Transaction

class TestBudget(unittest.TestCase):
    def setUp(self):
        self.budget = Budget()
        self.t1 = Transaction(1000, "Wynagrodzenie", "2025-06-01", "Wypłata")
        self.t2 = Transaction(-200, "Jedzenie", "2025-06-01", "Pizza")
        self.t3 = Transaction(-50, "Transport", "2025-07-01", "Bilet")

        self.budget.add_transaction(self.t1)
        self.budget.add_transaction(self.t2)
        self.budget.add_transaction(self.t3)

    def test_add_transaction_valid(self):
        self.assertEqual(len(self.budget.transactions), 3)

    def test_add_transaction_invalid_type(self):
        with self.assertRaises(TypeError):
            self.budget.add_transaction("not_a_transaction")

    def test_edit_transaction_valid(self):
        new_t = Transaction(-300, "Zakupy", "2025-06-01", "Nowy")
        self.budget.edit_transaction(1, new_t)
        self.assertEqual(self.budget.transactions[1].category, "Zakupy")

    def test_edit_transaction_invalid_index(self):
        with self.assertRaises(IndexError):
            self.budget.edit_transaction(5, self.t1)

    def test_delete_transaction_valid(self):
        self.budget.delete_transaction(1)
        self.assertEqual(len(self.budget.transactions), 2)

    def test_delete_transaction_invalid_index(self):
        with self.assertRaises(IndexError):
            self.budget.delete_transaction(10)

    def test_get_monthly_summary(self):
        summary = self.budget.get_monthly_summary()
        self.assertEqual(summary["2025-06"], 800)
        self.assertEqual(summary["2025-07"], -50)

    def test_get_category_summary(self):
        summary = self.budget.get_category_summary()
        self.assertEqual(summary["Wynagrodzenie"], 1000)
        self.assertEqual(summary["Jedzenie"], -200)

    def test_get_total_income(self):
        self.assertEqual(self.budget.get_total_income(), 1000)

    def test_get_total_expense(self):
        self.assertEqual(self.budget.get_total_expense(), -250)

    def test_get_monthly_balance(self):
        balance = self.budget.get_monthly_balance()
        self.assertEqual(balance["2025-06"], 800)
        self.assertEqual(balance["2025-07"], -50)

    def test_get_monthly_income_expense(self):
        result = self.budget.get_monthly_income_expense()
        self.assertEqual(result["2025-06"], [1000, -200])
        self.assertEqual(result["2025-07"], [0, -50])

if __name__ == "__main__":
    unittest.main()
