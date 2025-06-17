# tests/test_logic.py
import unittest
from logic import Transaction, Budget

class TestTransaction(unittest.TestCase):
    def test_valid_transaction(self):
        t = Transaction(100, "Jedzenie", "2025-06-15", "Obiad")
        self.assertEqual(t.amount, 100)
        self.assertEqual(t.category, "Jedzenie")
        self.assertEqual(t.date.strftime("%Y-%m-%d"), "2025-06-15")
        self.assertEqual(str(t), "2025-06-15 | Jedzenie | 100.00 zł | Obiad")

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            Transaction(100, "Transport", "15-06-2025")

    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            Transaction("abc", "Zakupy", "2025-06-01")

class TestBudget(unittest.TestCase):
    def setUp(self):
        self.budget = Budget()
        self.t1 = Transaction(1000, "Wynagrodzenie", "2025-06-01")
        self.t2 = Transaction(-200, "Jedzenie", "2025-06-03")
        self.budget.add_transaction(self.t1)
        self.budget.add_transaction(self.t2)

    def test_add_transaction_type_check(self):
        with self.assertRaises(TypeError):
            self.budget.add_transaction("nieprawidłowy obiekt")

    def test_get_monthly_balance(self):
        balance = self.budget.get_monthly_balance()
        self.assertEqual(balance["2025-06"], 800)

    def test_get_category_summary(self):
        summary = self.budget.get_category_summary()
        self.assertEqual(summary["Wynagrodzenie"], 1000)
        self.assertEqual(summary["Jedzenie"], -200)

if __name__ == "__main__":
    unittest.main()
