def zapisz_raport_do_pliku(budget, filename="raport.txt"):
    try:
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write("Miesięczne podsumowanie:\n")
            for month, total in budget.get_monthly_balance().items():
                file.write(f"{month}: {total:.2f} zł\n")

            file.write("\nPodsumowanie wg kategorii:\n")
            for cat, total in budget.get_category_summary().items():
                file.write(f"{cat}: {total:.2f} zł\n")

        print(f"Raport zapisany do pliku '{filename}'")
    except Exception as e:
        print(f"Błąd zapisu raportu: {e}")
