import matplotlib.pyplot as plt

def pokaz_saldo_miesieczne(balance_dict):
    if not balance_dict:
        print("Brak danych do analizy")
        return

    months = list(balance_dict.keys())
    values = list(balance_dict.values())

    plt.figure(figsize=(6, 4))
    plt.bar(months, values, color='skyblue')
    plt.title("Saldo miesięczne")
    plt.xlabel("Miesiąc")
    plt.ylabel("Saldo")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("saldo_miesieczne.png")
    plt.show()

def pokaz_podsumowanie_kategorii(summary_dict):
    if not summary_dict:
        print("Brak danych do analizy")
        return

    categories = list(summary_dict.keys())
    values = list(summary_dict.values())

    plt.figure(figsize=(6, 4))
    plt.barh(categories, values, color='lightgreen')
    plt.title("Suma według kategorii")
    plt.xlabel("Suma")
    plt.ylabel("Kategoria")
    plt.tight_layout()
    plt.savefig("podsumowanie_kategorii.png")
    plt.show()
