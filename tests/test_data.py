import unittest
import os
from data import save_transactions_to_csv, load_transactions_from_csv
from logic import Transaction

class TestDataHandling(unittest.TestCase):
    def setUp(self):
        self.test_file = "data/test_transactions.csv"
        self.transactions = [
            Transaction(100.0, "Jedzenie", "2025-06-01", "Obiad"),
            Transaction(-50.0, "Transport", "2025-06-02", "Bilet")
        ]

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load_transactions(self):
        save_transactions_to_csv(self.transactions, self.test_file)
        loaded = load_transactions_from_csv(self.test_file)

        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].amount, 100.0)
        self.assertEqual(loaded[0].category, "Jedzenie")
        self.assertEqual(loaded[0].description, "Obiad")
        self.assertEqual(loaded[1].amount, -50.0)
        self.assertEqual(loaded[1].category, "Transport")

    def test_load_nonexistent_file_returns_empty_list(self):
        result = load_transactions_from_csv("data/nonexistent_file.csv")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_save_empty_transaction_list(self):
        empty_file = "data/empty_transactions.csv"
        save_transactions_to_csv([], empty_file)
        loaded = load_transactions_from_csv(empty_file)
        self.assertEqual(loaded, [])
        os.remove(empty_file)

if __name__ == "__main__":
    unittest.main()
