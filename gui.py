import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from logic import Budget, Transaction
from data import save_transactions_to_json, load_transactions_from_json
from auth import login_user, register_user
from utils import recursive_sum, log_action
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budżet osobisty - GUI")
        self.root.geometry("400x250")
        self.user = None
        self.budget = Budget()
        self.login_screen()

    def login_screen(self):
        self.clear_window()

        tk.Label(self.root, text="Zaloguj się lub zarejestruj").pack(pady=10)
        tk.Label(self.root, text="Użytkownik:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        tk.Label(self.root, text="Hasło:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Zaloguj", command=self.login).pack(pady=5)
        tk.Button(self.root, text="Zarejestruj", command=self.register).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = login_user(username, password)
        if user:
            self.user = user
            self.budget.transactions = load_transactions_from_json(f"data/{user}_transactions.json")
            self.main_screen()
        else:
            messagebox.showerror("Błąd", "Niepoprawne dane logowania")

    def register(self):
        username = self.username_entry.get()
        password = self.username_entry.get()
        user = register_user(username, password)
        if user:
            messagebox.showinfo("Sukces", "Zarejestrowano pomyślnie")
        else:
            messagebox.showerror("Błąd", "Użytkownik już istnieje")

    def main_screen(self):
        self.root.geometry("900x600")
        self.clear_window()
        tk.Label(self.root, text=f"Witaj, {self.user}", font=("Arial", 14)).pack(pady=10)

        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=5)

        tk.Label(form_frame, text="Kwota").grid(row=0, column=0)
        self.amount_entry = tk.Entry(form_frame)
        self.amount_entry.grid(row=0, column=1)

        tk.Label(form_frame, text="Kategoria").grid(row=1, column=0)
        self.category_entry = tk.Entry(form_frame)
        self.category_entry.grid(row=1, column=1)

        tk.Label(form_frame, text="Data (RRRR-MM-DD)").grid(row=2, column=0)
        self.date_entry = tk.Entry(form_frame)
        self.date_entry.grid(row=2, column=1)

        tk.Label(form_frame, text="Opis").grid(row=3, column=0)
        self.description_entry = tk.Entry(form_frame)
        self.description_entry.grid(row=3, column=1)

        tk.Button(form_frame, text="Dodaj transakcję", command=self.add_transaction).grid(row=4, column=0, columnspan=2, pady=5)

        frame = tk.Frame(self.root)
        frame.pack(pady=5)

        self.tree = ttk.Treeview(frame, columns=("Kwota", "Kategoria", "Data", "Opis"), show='headings', height=10)
        for col in ("Kwota", "Kategoria", "Data", "Opis"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.grid(row=0, column=0)

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        action_frame = tk.Frame(self.root)
        action_frame.pack(pady=5)
        tk.Button(action_frame, text="Edytuj zaznaczoną", command=self.edit_selected_transaction).pack(side=tk.LEFT, padx=5)
        tk.Button(action_frame, text="Usuń zaznaczoną", command=self.delete_selected_transaction).pack(side=tk.LEFT, padx=5)
        tk.Button(action_frame, text="Pokaż saldo miesięczne", command=self.show_analysis).pack(side=tk.LEFT, padx=5)
        tk.Button(action_frame, text="Pokaż sumy kategorii", command=self.show_category_summary).pack(side=tk.LEFT, padx=5)
        tk.Button(action_frame, text="Rekurencyjna suma transakcji", command=self.show_recursive_sum).pack(side=tk.LEFT, padx=5)
        tk.Button(action_frame, text="Pokaż unikalne kategorie", command=self.show_unique_categories).pack(side=tk.LEFT, padx=5)
        tk.Button(action_frame, text="Średnia transakcji", command=self.show_average_transaction).pack(side=tk.LEFT, padx=5)

        self.refresh_table()
        tk.Button(self.root, text="Wyloguj", command=self.logout).pack(pady=10)

        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=5)

        tk.Label(search_frame, text="Wyszukaj:").pack(side=tk.LEFT)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(search_frame, text="Szukaj", command=self.search_transactions).pack(side=tk.LEFT)
        tk.Button(search_frame, text="Pokaż wszystkie", command=self.refresh_table).pack(side=tk.LEFT, padx=5)

    def add_transaction(self):
        try:
            amount = float(self.amount_entry.get())
            category = self.category_entry.get()
            date = self.date_entry.get()
            description = self.description_entry.get()

            assert amount != 0, "Kwota nie może być zerowa"

            transaction = Transaction(amount, category, date, description)
            self.budget.add_transaction(transaction)
            self.refresh_table()
        except AssertionError as ae:
            messagebox.showerror("Błąd", f"Błąd danych: {ae}")
        except Exception as e:
            messagebox.showerror("Błąd", str(e))

    def edit_selected_transaction(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Uwaga", "Nie zaznaczono żadnej transakcji")
            return
        index = self.tree.index(selected[0])
        try:
            amount = float(self.amount_entry.get())
            category = self.category_entry.get()
            date = self.date_entry.get()
            description = self.description_entry.get()
            transaction = Transaction(amount, category, date, description)
            self.budget.transactions[index] = transaction
            self.refresh_table()
        except Exception as e:
            messagebox.showerror("Błąd", str(e))

    def delete_selected_transaction(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Uwaga", "Nie zaznaczono żadnej transakcji")
            return
        index = self.tree.index(selected[0])
        del self.budget.transactions[index]
        self.refresh_table()

    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for t in self.budget.transactions:
            row = (t.amount, t.category, t.date, t.description)
            self.tree.insert("", tk.END, values=row)

    def search_transactions(self):
        query = self.search_entry.get().lower()
        if not query:
            messagebox.showwarning("Brak danych", "Wprowadź tekst do wyszukania.")
            return

        filtered = [
            t for t in self.budget.transactions
            if query in str(t.amount).lower()
            or query in t.category.lower()
            or query in t.description.lower()
            or query in str(t.date)
        ]
        self.tree.delete(*self.tree.get_children())
        for t in filtered:
            self.tree.insert("", tk.END, values=(t.amount, t.category, t.date, t.description))

    @log_action
    def show_recursive_sum(self):
        total = recursive_sum(self.budget.transactions)
        messagebox.showinfo("Suma (rekurencyjna)", f"Łączna kwota wszystkich transakcji: {total:.2f} zł")

    def show_unique_categories(self):
        categories = {t.category for t in self.budget.transactions}
        messagebox.showinfo("Unikalne kategorie", "\n".join(categories) if categories else "Brak danych.")

    def show_average_transaction(self):
        try:
            kwoty = list(map(lambda t: t.amount, self.budget.transactions))
            if not kwoty:
                messagebox.showinfo("Średnia", "Brak danych do analizy.")
                return
            srednia = sum(kwoty) / len(kwoty)
            messagebox.showinfo("Średnia transakcji", f"Średnia wartość transakcji: {srednia:.2f} zł")
        except Exception as e:
            messagebox.showerror("Błąd", str(e))

    def show_analysis(self):
        balance = self.budget.get_monthly_balance()
        if not balance:
            messagebox.showinfo("Analiza", "Brak danych do analizy")
            return

        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        months = list(balance.keys())
        values = list(balance.values())
        ax.bar(months, values, color='skyblue')
        ax.set_title("Saldo miesięczne")
        ax.set_xlabel("Miesiąc")
        ax.set_ylabel("Saldo")
        ax.tick_params(axis='x', rotation=45)
        fig.savefig("saldo_miesieczne.png")
        self.show_plot(fig, "Saldo miesięczne")

    def show_category_summary(self):
        summary = self.budget.get_category_summary()
        if not summary:
            messagebox.showinfo("Analiza", "Brak danych do analizy")
            return

        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        categories = list(summary.keys())
        values = list(summary.values())
        ax.barh(categories, values, color='lightgreen')
        ax.set_title("Suma według kategorii")
        ax.set_xlabel("Suma")
        ax.set_ylabel("Kategoria")
        fig.savefig("suma_kategorii.png")
        self.show_plot(fig, "Suma według kategorii")

    def show_plot(self, fig, title):
        window = tk.Toplevel(self.root)
        window.title(title)

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        def save_plot():
            filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if filepath:
                fig.savefig(filepath)
                messagebox.showinfo("Zapisano", f"Wykres zapisano jako: {filepath}")

        save_button = tk.Button(window, text="Zapisz wykres jako PNG", command=save_plot)
        save_button.pack(pady=5)

    def logout(self):
        save_transactions_to_json(self.budget.transactions, f"data/{self.user}_transactions.json")
        self.user = None
        self.budget = Budget()
        self.login_screen()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()