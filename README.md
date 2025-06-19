# Budżet osobisty – Instrukcja obsługi

## Opis

Aplikacja służy do zarządzania budżetem osobistym z wykorzystaniem graficznego interfejsu użytkownika (GUI). Pozwala użytkownikowi rejestrować, przeglądać i analizować swoje transakcje finansowe. Dane przechowywane są w plikach `.json`, osobno dla każdego użytkownika.

### Główne funkcje:
- logowanie i rejestracja z użyciem haszowania SHA-256,
- dodawanie, edytowanie i usuwanie transakcji,
- wykresy miesięcznego salda oraz podsumowania kategorii,
- średnia i rekurencyjna suma transakcji,
- filtrowanie i wyszukiwanie transakcji,
- zapis wykresów do plików `.png`,
- automatyczne zapisywanie danych użytkownika.

---

## Uruchomienie aplikacji

1. **Zainstaluj wymagane biblioteki**:

```bash
pip install matplotlib
```

2. **Uruchom program**:

```bash
python gui.py
```

---

## Logowanie i rejestracja

- Przy pierwszym uruchomieniu pojawia się ekran logowania.
- Użytkownik może się zalogować lub utworzyć nowe konto.
- Dane logowania zapisywane są w pliku:  
  `data/users.json`
- Dane transakcji zapisywane są osobno dla każdego użytkownika w pliku:  
  `data/<login>_transactions.json`

---

## Funkcjonalności po zalogowaniu

- **Dodaj transakcję** – wpisz kwotę, kategorię, datę (YYYY-MM-DD), opis.
- **Edytuj/usuń transakcję** – zaznacz transakcję w tabeli.
- **Saldo miesięczne** – wykres pokazujący sumę transakcji z każdego miesiąca.
- **Suma wg kategorii** – wykres pokazujący rozkład wydatków/przychodów.
- **Średnia transakcji** – oblicza średnią wartość transakcji.
- **Rekurencyjna suma** – oblicza sumę rekurencyjnie.
- **Unikalne kategorie** – pokazuje wszystkie kategorie transakcji.
- **Wyszukiwanie** – filtruje po dowolnym fragmencie tekstu.
- **Zapis wykresu do PNG** – każdy wykres można zapisać do pliku.
- **Wylogowanie** – zapisuje dane i wraca do ekranu logowania.

---

## Struktura projektu

```
├── gui.py               # Główny plik uruchamiający aplikację
├── logic.py             # Klasy Transaction, Budget, IncomeTransaction
├── data.py              # Obsługa zapisu/odczytu transakcji z JSON
├── auth.py              # Rejestracja i logowanie użytkowników
├── charts.py            # Tworzenie wykresów (matplotlib)
├── utils.py             # Raporty, logowanie akcji, rekurencja
├── data/                # Folder z plikami JSON użytkowników
└── tests/               # Folder z testami jednostkowymi
```

---

## Bezpieczeństwo

- Hasła są haszowane przy użyciu SHA-256.
- Dane zapisywane są lokalnie w folderze `data/`, bez udziału internetu.
- Pliki transakcji użytkownika są odseparowane i nazwane zgodnie z loginem.

---

## Testowanie

W katalogu `tests/` znajdują się testy `unittest`, obejmujące:

- funkcje z plików `logic.py`, `auth.py`, `data.py`,
- testy GUI z wykorzystaniem `unittest.mock`,
- testy wykresów,
- testy zapisu i ładowania danych użytkownika.

---

## Wymagania

- Python 3.9 lub nowszy
- Biblioteki:
  - `tkinter`
  - `matplotlib`

---

## Wnioski

Aplikacja została zaprojektowana jako graficzny system do zarządzania finansami osobistymi. Oferuje wszystkie podstawowe funkcjonalności potrzebne do śledzenia dochodów i wydatków. Zastosowanie formatu JSON pozwala na przechowywanie danych w sposób przejrzysty i rozszerzalny. Projekt charakteryzuje się modularną strukturą i został uzupełniony o testy jednostkowe, co ułatwia jego dalszy rozwój i konserwację.
