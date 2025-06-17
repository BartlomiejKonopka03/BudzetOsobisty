import unittest
import os
from utils import zapisz_raport_do_pliku
from logic import Transaction, Budget

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_raport.txt"
        self.budget = Budget()
        self.budget.add_transaction(Transaction(5000, "Wynagrodzenie", "2025-06-01"))
        self.budget.add_transaction(Transaction(-200, "Jedzenie", "2025-06-02"))
        self.budget.add_transaction(Transaction(-300, "Transport", "2025-06-03"))

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_zapisz_raport_do_pliku(self):
        zapisz_raport_do_pliku(self.budget, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

        with open(self.test_file, "r", encoding="utf-8") as file:
            content = file.read()
            self.assertIn("Miesięczne podsumowanie", content)
            self.assertIn("2025-06: 4500.00 zł", content)
            self.assertIn("Podsumowanie wg kategorii", content)
            self.assertIn("Jedzenie: -200.00 zł", content)
            self.assertIn("Transport: -300.00 zł", content)

if __name__ == "__main__":
    unittest.main()
