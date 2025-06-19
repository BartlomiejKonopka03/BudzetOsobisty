import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from gui import BudgetApp
from logic import Transaction

class TestBudgetAppGUI(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = BudgetApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_initial_screen_title_and_geometry(self):
        self.assertEqual(self.root.title(), "Budżet osobisty - GUI")
        self.assertTrue(hasattr(self.root, 'geometry'))

    def test_login_screen_widgets_exist(self):
        self.app.login_screen()
        found_labels = [w for w in self.root.winfo_children() if isinstance(w, tk.Label)]
        found_entries = [w for w in self.root.winfo_children() if isinstance(w, tk.Entry)]
        found_buttons = [w for w in self.root.winfo_children() if isinstance(w, tk.Button)]

        self.assertGreaterEqual(len(found_labels), 2)
        self.assertGreaterEqual(len(found_entries), 2)
        self.assertGreaterEqual(len(found_buttons), 2)

    @patch('gui.login_user')
    @patch('gui.load_transactions_from_csv', return_value=[])
    def test_successful_login_transitions_to_main_screen(self, mock_load, mock_login):
        mock_login.return_value = "testuser"
        self.app.username_entry.insert(0, "testuser")
        self.app.password_entry.insert(0, "password")
        self.app.login()
        self.assertEqual(self.app.user, "testuser")
        self.assertTrue(hasattr(self.app, 'amount_entry'))

    @patch('gui.login_user', return_value=None)
    @patch('tkinter.messagebox.showerror')
    def test_unsuccessful_login_shows_error(self, mock_showerror, mock_login):
        self.app.username_entry.insert(0, "wrong")
        self.app.password_entry.insert(0, "wrong")
        self.app.login()
        mock_showerror.assert_called_once_with("Błąd", "Niepoprawne dane logowania")

    @patch("tkinter.messagebox.showinfo")
    def test_show_average_transaction(self, mock_showinfo):
        self.app.budget.transactions = [
            Transaction(100, "jedzenie", "2024-01-01", "pizza"),
            Transaction(200, "rozrywka", "2024-01-02", "kino")
        ]
        self.app.show_average_transaction()
        mock_showinfo.assert_called_with("Średnia transakcji", "Średnia wartość transakcji: 150.00 zł")

    @patch("tkinter.messagebox.showinfo")
    def test_logout_resets_user(self, mock_showinfo):
        self.app.user = "test_user"
        self.app.logout()
        self.assertIsNone(self.app.user)

if __name__ == '__main__':
    unittest.main()
