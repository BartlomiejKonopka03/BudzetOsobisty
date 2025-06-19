import matplotlib.pyplot as plt

# Funkcja generuje wykres słupkowy przedstawiający saldo dla każdego miesiąca.
# Dane wejściowe: słownik w formacie {"YYYY-MM": suma_za_miesiąc}
def pokaz_saldo_miesieczne(balance_dict):
    if not balance_dict:
        print("Brak danych do analizy")
        return

    months = list(balance_dict.keys())   # lista miesięcy (np. "2025-06")
    values = list(balance_dict.values()) # lista odpowiadających sald

    plt.figure(figsize=(6, 4))
    plt.bar(months, values, color='skyblue')  # wykres słupkowy
    plt.title("Saldo miesięczne")
    plt.xlabel("Miesiąc")
    plt.ylabel("Saldo")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("saldo_miesieczne.png")  # zapis wykresu do pliku
    plt.show()                           # wyświetlenie wykresu

# Funkcja generuje wykres poziomy pokazujący sumę transakcji dla każdej kategorii.
# Dane wejściowe: słownik w formacie {"Kategoria": suma}
def pokaz_podsumowanie_kategorii(summary_dict):
    if not summary_dict:
        print("Brak danych do analizy")
        return

    categories = list(summary_dict.keys())   # lista kategorii
    values = list(summary_dict.values())     # odpowiadające sumy

    plt.figure(figsize=(6, 4))
    plt.barh(categories, values, color='lightgreen')  # poziomy wykres słupkowy
    plt.title("Suma według kategorii")
    plt.xlabel("Suma")
    plt.ylabel("Kategoria")
    plt.tight_layout()
    plt.savefig("podsumowanie_kategorii.png")  # zapis wykresu do pliku
    plt.show()                                 # wyświetlenie wykresu
